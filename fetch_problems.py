#!/usr/bin/env python3
"""Generate a local LeetCode study repository."""

import argparse
import ast
import html
from html.parser import HTMLParser
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
GRAPHQL_URL = "https://leetcode.com/graphql"
NEETCODE_URL = (
    "https://raw.githubusercontent.com/neetcode-gh/leetcode/main/"
    ".problemSiteData.json"
)
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    topicTags { name }
    content
    exampleTestcases
    codeSnippets { langSlug code }
    metaData
  }
}
"""
PROBLEMSET_QUERY = """
query problemsetQuestionList(
  $categorySlug: String,
  $limit: Int,
  $skip: Int,
  $filters: QuestionListFilterInput
) {
  problemsetQuestionList(
    categorySlug: $categorySlug,
    limit: $limit,
    skip: $skip,
    filters: $filters
  ) {
    questions {
      frontendQuestionId
      title
      titleSlug
      difficulty
      paidOnly
      topicTags { name }
    }
  }
}
"""


class HTMLToMarkdown(HTMLParser):
    """A small converter for the markup used in LeetCode statements."""

    def __init__(self) -> None:
        HTMLParser.__init__(self, convert_charrefs=True)
        self.parts = []  # type: List[str]
        self.pre_depth = 0
        self.list_stack = []  # type: List[Dict[str, Any]]
        self.list_item_depth = 0
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attributes = dict(attrs)
        if tag in ("script", "style"):
            self.ignored_depth += 1
            return
        if self.ignored_depth:
            return
        if tag == "p":
            if self.list_item_depth:
                if self.parts and not (
                    self.parts[-1].endswith("\n") or self.parts[-1].endswith(" ")
                ):
                    self.parts.append("\n")
            else:
                self.parts.append("\n\n")
        elif tag in ("strong", "b"):
            self.parts.append("**")
        elif tag in ("em", "i"):
            self.parts.append("*")
        elif tag == "code" and not self.pre_depth:
            self.parts.append("`")
        elif tag == "pre":
            self.parts.append("\n\n```\n")
            self.pre_depth += 1
        elif tag in ("ul", "ol"):
            self.list_stack.append({"kind": tag, "next": 1})
            if not self.parts or not self.parts[-1].endswith("\n"):
                self.parts.append("\n")
        elif tag == "li":
            depth = max(0, len(self.list_stack) - 1)
            prefix = "  " * depth
            if self.list_stack and self.list_stack[-1]["kind"] == "ol":
                item_number = self.list_stack[-1]["next"]
                self.list_stack[-1]["next"] = item_number + 1
                marker = str(item_number) + ". "
            else:
                marker = "- "
            if self.parts and not self.parts[-1].endswith("\n"):
                self.parts.append("\n")
            self.parts.append(prefix + marker)
            self.list_item_depth += 1
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "img":
            source = attributes.get("src") or ""
            self.parts.append("![](" + source + ")")
        elif tag == "sup":
            self.parts.append("^")
        elif tag == "sub":
            self.parts.append("<sub>")
        elif tag in ("h1", "h2", "h3", "h4"):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "blockquote":
            self.parts.append("\n\n> ")
        elif tag == "hr":
            self.parts.append("\n\n---\n\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self.ignored_depth:
            self.ignored_depth -= 1
            return
        if self.ignored_depth:
            return
        if tag == "p":
            if self.list_item_depth:
                if not self.parts or not self.parts[-1].endswith("\n"):
                    self.parts.append("\n")
            else:
                self.parts.append("\n\n")
        elif tag in ("strong", "b"):
            trailing_space = ""
            if self.parts and not self.pre_depth:
                trailing = re.search(r"[ \t]+$", self.parts[-1])
                if trailing:
                    self.parts[-1] = self.parts[-1][: -len(trailing.group(0))]
                    trailing_space = " "
            self.parts.append("**" + trailing_space)
        elif tag in ("em", "i"):
            trailing_space = ""
            if self.parts and not self.pre_depth:
                trailing = re.search(r"[ \t]+$", self.parts[-1])
                if trailing:
                    self.parts[-1] = self.parts[-1][: -len(trailing.group(0))]
                    trailing_space = " "
            self.parts.append("*" + trailing_space)
        elif tag == "code" and not self.pre_depth:
            self.parts.append("`")
        elif tag == "pre":
            if self.pre_depth:
                self.pre_depth -= 1
            self.parts.append("\n```\n\n")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            if not self.list_stack:
                self.parts.append("\n")
        elif tag == "li":
            if self.list_item_depth:
                self.list_item_depth -= 1
            if not self.parts or not self.parts[-1].endswith("\n"):
                self.parts.append("\n")
        elif tag in ("h1", "h2", "h3", "h4", "blockquote"):
            self.parts.append("\n\n")
        elif tag == "sub":
            self.parts.append("</sub>")

    def handle_data(self, data: str) -> None:
        if self.ignored_depth:
            return
        data = data.replace("\xa0", " ")
        if self.pre_depth:
            self.parts.append(data)
        else:
            normalized = re.sub(r"\s+", " ", data)
            if self.parts and self.parts[-1].endswith("\n"):
                normalized = normalized.lstrip()
            if normalized:
                self.parts.append(normalized)

    def markdown(self) -> str:
        text = html.unescape("".join(self.parts)).replace("\xa0", " ")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", text)
        return text.strip()


class LeetCodeClient:
    def __init__(self, delay: float, refresh: bool) -> None:
        self.delay = delay
        self.refresh = refresh
        self.network_calls = 0

    def _network_json(
        self, url: str, payload: Optional[Dict[str, Any]] = None
    ) -> Any:
        headers = {"User-Agent": USER_AGENT}
        if payload is not None:
            headers["Content-Type"] = "application/json"
            headers["Referer"] = "https://leetcode.com"
            data = json.dumps(payload).encode("utf-8")
        else:
            data = None
        for attempt in range(4):
            if self.network_calls and self.delay:
                time.sleep(self.delay)
            self.network_calls += 1
            request = Request(url, data=data, headers=headers)
            try:
                with urlopen(request, timeout=30) as response:
                    return json.loads(response.read().decode("utf-8"))
            except HTTPError as error:
                should_retry = error.code == 429 or 500 <= error.code <= 599
                if not should_retry or attempt == 3:
                    raise
            except URLError:
                if attempt == 3:
                    raise
            time.sleep(2 ** attempt)
        raise RuntimeError("Request retries exhausted for " + url)

    def fetch_json(
        self,
        url: str,
        cache_path: Path,
        payload: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if cache_path.exists() and not self.refresh:
            try:
                return json.loads(cache_path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                pass
        result = self._network_json(url, payload)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return result


def load_neetcode(client: LeetCodeClient) -> List[Dict[str, Any]]:
    path = ROOT / ".cache" / "neetcode.json"
    data = client.fetch_json(NEETCODE_URL, path)
    if isinstance(data, dict):
        data = data.get("problems", data.get("data", []))
    if not isinstance(data, list):
        raise ValueError("Unexpected NeetCode data format")
    return data


def neetcode_by_slug(entries: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    result = {}  # type: Dict[str, Dict[str, Any]]
    for entry in entries:
        link = str(entry.get("link") or "").strip("/")
        slug = link.rsplit("/", 1)[-1]
        if slug:
            result[slug] = entry
    return result


def numeric_id(problem: Dict[str, Any]) -> int:
    value = problem.get("questionFrontendId") or problem.get("frontendQuestionId")
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def problem_directory_name(problem_id: int, slug: str, difficulty: str) -> str:
    return "%04d-%s-%s" % (problem_id, slug, str(difficulty).lower())


def parse_problem_directory(
    directory_name: str,
) -> Optional[Tuple[int, str, Optional[str]]]:
    match = re.match(r"^(\d{4,})-(.+?)-(easy|medium|hard)$", directory_name)
    if match:
        return int(match.group(1)), match.group(2), match.group(3)
    match = re.match(r"^(\d{4,})-(.+)$", directory_name)
    if match:
        return int(match.group(1)), match.group(2), None
    return None


def migrate_problem_directory(
    problem_id: int, slug: str, difficulty: str
) -> Path:
    destination = ROOT / problem_directory_name(problem_id, slug, difficulty)
    if destination.exists():
        return destination

    legacy_name = "%04d-%s" % (problem_id, slug)
    legacy_path = ROOT / legacy_name
    candidates = []  # type: List[Path]
    if legacy_path.is_dir():
        candidates.append(legacy_path)
    for path in ROOT.iterdir():
        parsed = parse_problem_directory(path.name)
        if (
            path.is_dir()
            and parsed is not None
            and parsed[0] == problem_id
            and parsed[1] == slug
            and path.name != destination.name
            and path not in candidates
        ):
            candidates.append(path)
    if candidates:
        source = candidates[0]
        source.rename(destination)
        print("Migrated %s to %s" % (source.name, destination.name))
    return destination


def list_all_problems(
    client: LeetCodeClient, batch_size: int
) -> List[Dict[str, Any]]:
    page_size = max(100, batch_size)
    problems = []  # type: List[Dict[str, Any]]
    skip = 0
    while True:
        payload = {
            "query": PROBLEMSET_QUERY,
            "variables": {
                "categorySlug": "",
                "limit": page_size,
                "skip": skip,
                "filters": {},
            },
        }
        cache_path = (
            ROOT
            / ".cache"
            / "problemset"
            / ("page-%d-%d.json" % (skip, page_size))
        )
        response = client.fetch_json(GRAPHQL_URL, cache_path, payload)
        try:
            page = response["data"]["problemsetQuestionList"]["questions"]
        except (KeyError, TypeError):
            raise ValueError("Unexpected problemset response: " + repr(response))
        problems.extend(page)
        if len(page) < page_size:
            break
        skip += page_size
    return sorted(problems, key=lambda item: (numeric_id(item), item.get("titleSlug", "")))


def select_problems(
    args: argparse.Namespace,
    client: LeetCodeClient,
    neetcode_entries: List[Dict[str, Any]],
) -> List[Tuple[str, Optional[int]]]:
    if args.slugs:
        return [(slug.strip(), None) for slug in args.slugs.split(",") if slug.strip()]
    if args.list_name == "all":
        items = [
            (str(item.get("titleSlug", "")), numeric_id(item))
            for item in list_all_problems(client, args.batch_size)
            if item.get("titleSlug")
        ]
    else:
        flag = "blind75" if args.list_name == "blind75" else "neetcode150"
        items = []
        for entry in neetcode_entries:
            if entry.get(flag):
                slug = str(entry.get("link") or "").strip("/")
                if slug:
                    items.append((slug.rsplit("/", 1)[-1], None))
    start = args.start
    return items[start : start + args.batch_size]


def get_question(client: LeetCodeClient, slug: str) -> Optional[Dict[str, Any]]:
    cache_path = ROOT / ".cache" / "questions" / (slug + ".json")
    payload = {
        "query": QUESTION_QUERY,
        "variables": {"titleSlug": slug},
    }
    response = client.fetch_json(GRAPHQL_URL, cache_path, payload)
    try:
        question = response["data"]["question"]
    except (KeyError, TypeError):
        question = response.get("question") if isinstance(response, dict) else None
    return question


def load_curated(slug: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    json_path = ROOT / "curated" / (slug + ".json")
    py_path = ROOT / "curated" / (slug + ".py")
    notes = None
    solution = None
    if json_path.exists():
        notes = json.loads(json_path.read_text(encoding="utf-8"))
    if py_path.exists():
        solution = py_path.read_text(encoding="utf-8").rstrip() + "\n"
    return notes, solution


def build_video(
    client: LeetCodeClient,
    videos: Dict[str, Any],
    neetcode_entry: Optional[Dict[str, Any]],
    question_id: int,
    title: str,
) -> Tuple[str, str, bool]:
    video_id = str((neetcode_entry or {}).get("video") or "").strip()
    if video_id:
        cached = videos.get(video_id)
        video_url = "https://www.youtube.com/watch?v=" + video_id
        if isinstance(cached, dict) and cached.get("title"):
            return str(cached["title"]), video_url, True
        oembed_url = (
            "https://www.youtube.com/oembed?"
            + urlencode({"url": video_url, "format": "json"})
        )
        try:
            data = client.fetch_json(
                oembed_url,
                ROOT / ".cache" / "videos-oembed" / (video_id + ".json"),
            )
            title_value = str(data.get("title") or "").strip()
            if title_value:
                videos[video_id] = {"title": title_value, "url": video_url}
                return title_value, video_url, True
        except (HTTPError, URLError, ValueError, OSError) as error:
            print("Video lookup failed for %s: %s" % (video_id, error))
    search_term = "leetcode %d %s neetcode" % (question_id, title)
    search_url = (
        "https://www.youtube.com/results?"
        + urlencode({"search_query": search_term})
    )
    return "Search YouTube for " + search_term, search_url, False


def topic_names(question: Dict[str, Any]) -> List[str]:
    tags = question.get("topicTags") or []
    names = []
    for tag in tags:
        if isinstance(tag, dict) and tag.get("name"):
            names.append(str(tag["name"]))
    return names


def problem_pattern(
    notes: Optional[Dict[str, Any]],
    neetcode_entry: Optional[Dict[str, Any]],
    topics: List[str],
) -> str:
    if notes and notes.get("pattern"):
        return str(notes["pattern"])
    if neetcode_entry and neetcode_entry.get("pattern"):
        return str(neetcode_entry["pattern"])
    if topics:
        return topics[0]
    return "Not specified"


def render_approach(notes: Optional[Dict[str, Any]]) -> str:
    if not notes:
        return "## Approach\n\n_Not written yet._\n"
    intuition = str(notes.get("intuition") or "_Not written yet._")
    brute = notes.get("brute_force") or {}
    optimal = notes.get("optimal") or {}
    brute_approach = str(brute.get("approach") or "_Not written yet._")
    optimal_approach = str(optimal.get("approach") or "_Not written yet._")
    edge_cases = notes.get("edge_cases") or []
    edge_text = "\n".join("- " + str(case) for case in edge_cases)
    if not edge_text:
        edge_text = "_Not written yet._"
    return (
        "## Approach\n\n"
        "### Intuition\n\n%s\n\n"
        "### Brute Force\n\n%s\n\n"
        "### Optimal\n\n%s\n\n"
        "| Approach | Time | Space |\n"
        "| --- | --- | --- |\n"
        "| Brute Force | %s | %s |\n"
        "| Optimal | %s | %s |\n\n"
        "### Edge cases\n\n%s\n"
        % (
            intuition,
            brute_approach,
            optimal_approach,
            brute.get("time", "TBD"),
            brute.get("space", "TBD"),
            optimal.get("time", "TBD"),
            optimal.get("space", "TBD"),
            edge_text,
        )
    )


def render_problem_readme(
    question: Dict[str, Any],
    pattern: str,
    video_title: str,
    video_url: str,
    is_specific_video: bool,
    notes: Optional[Dict[str, Any]],
    premium_description: Optional[str] = None,
) -> str:
    problem_id = int(question["questionFrontendId"])
    title = str(question.get("title") or "")
    slug = str(question.get("titleSlug") or "")
    difficulty = str(question.get("difficulty") or "Unknown")
    topics = topic_names(question)
    problem_heading = "## Problem\n\n"
    if premium_description is not None:
        description = premium_description.strip()
    else:
        content = HTMLToMarkdown()
        content.feed(str(question.get("content") or ""))
        description = content.markdown() or "_Problem description unavailable._"
    video_label = video_title if is_specific_video else "YouTube search: " + video_title
    premium_notice = (
        "> 🔒 LeetCode Premium problem — statement paraphrased.\n\n"
        if premium_description is not None
        else ""
    )
    return (
        "# %d. %s\n\n"
        "%s"
        "**Difficulty:** %s  \n"
        "**Tags:** %s  \n"
        "**Pattern:** %s  \n"
        "**LeetCode:** [https://leetcode.com/problems/%s/]"
        "(https://leetcode.com/problems/%s/)\n\n"
        "%s%s\n\n"
        "## Video Explanation\n\n[%s](%s)\n\n"
        "%s"
        % (
            problem_id,
            title,
            premium_notice,
            difficulty,
            ", ".join(topics) if topics else "None",
            pattern,
            slug,
            slug,
            problem_heading,
            description,
            video_label,
            video_url,
            render_approach(notes),
        )
    )


def solution_header(
    question: Dict[str, Any],
    pattern: str,
    video_url: str,
    notes: Optional[Dict[str, Any]],
) -> str:
    if notes:
        optimal = notes.get("optimal") or {}
        time_complexity = str(optimal.get("time") or "TBD")
        space_complexity = str(optimal.get("space") or "TBD")
    else:
        time_complexity = "TBD"
        space_complexity = "TBD"
    return (
        '"""\n'
        "LeetCode %s: %s\n"
        "Difficulty: %s\n"
        "Pattern: %s\n"
        "Video Reference: %s\n"
        "Complexity:\n"
        "    - Time: %s\n"
        "    - Space: %s\n"
        '"""\n\n'
        % (
            question["questionFrontendId"],
            question["title"],
            question.get("difficulty") or "Unknown",
            pattern,
            video_url,
            time_complexity,
            space_complexity,
        )
    )


def python3_snippet(question: Dict[str, Any]) -> str:
    snippets = question.get("codeSnippets") or []
    for snippet in snippets:
        if str(snippet.get("langSlug") or "").lower() == "python3":
            return str(snippet.get("code") or "").rstrip()
    return "class Solution:\n    pass"


def todo_solution(question: Dict[str, Any]) -> str:
    snippet = python3_snippet(question)
    converted_annotation = False
    for builtin, typing_name in (
        ("list", "List"),
        ("dict", "Dict"),
        ("set", "Set"),
        ("tuple", "Tuple"),
    ):
        snippet, replacements = re.subn(
            r"\b" + builtin + r"\s*\[", typing_name + "[", snippet
        )
        converted_annotation = converted_annotation or replacements > 0
    try:
        parsed = ast.parse(snippet)
        functions = [
            node
            for node in ast.walk(parsed)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        if functions:
            function = min(functions, key=lambda node: node.lineno)
            lines = snippet.splitlines()
            indent = len(lines[function.lineno - 1]) - len(
                lines[function.lineno - 1].lstrip()
            )
            lines[function.lineno : function.end_lineno] = [
                " " * (indent + 4) + "raise NotImplementedError"
            ]
            snippet = "\n".join(lines)
    except (SyntaxError, AttributeError, TypeError):
        lines = snippet.splitlines()
        for index, line in enumerate(lines):
            match = re.match(r"^(\s*)def\s+.*:\s*(?:#.*)?$", line)
            if not match:
                continue
            indent = len(match.group(1))
            end = index + 1
            while end < len(lines):
                if lines[end].strip():
                    current_indent = len(lines[end]) - len(lines[end].lstrip())
                    if current_indent <= indent:
                        break
                end += 1
            lines[index + 1 : end] = [
                " " * (indent + 4) + "raise NotImplementedError"
            ]
            snippet = "\n".join(lines)
            break
    if (
        converted_annotation
        or re.search(r"\b(List|Dict|Set|Tuple|Optional)\[", snippet)
    ) and "from typing" not in snippet:
        snippet = "from typing import *\n\n" + snippet
    examples = str(question.get("exampleTestcases") or "").splitlines()
    if examples:
        comments = "\n".join("# " + line for line in examples)
        example_comments = "# Example testcases from LeetCode:\n" + comments + "\n\n"
    else:
        example_comments = ""
    return (
        "# STATUS: TODO\n"
        + example_comments
        + snippet
        + "\n\n\nif __name__ == \"__main__\":\n"
        + "    print(\"TODO: not solved yet\")\n"
        + "    raise SystemExit(0)\n"
    )


def write_solution(
    path: Path,
    question: Dict[str, Any],
    header: str,
    curated_code: Optional[str],
    force: bool,
) -> None:
    if path.exists() and not force:
        existing = path.read_text(encoding="utf-8")
        if not (curated_code and "# STATUS: TODO" in existing):
            return
    contents = header + (
        curated_code if curated_code is not None else todo_solution(question)
    )
    path.write_text(contents, encoding="utf-8")


def load_video_cache() -> Dict[str, Any]:
    path = ROOT / ".cache" / "videos.json"
    if path.exists():
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(value, dict):
                return value
        except (OSError, ValueError):
            pass
    return {}


def save_video_cache(videos: Dict[str, Any]) -> None:
    path = ROOT / ".cache" / "videos.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(videos, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def generate_problem(
    client: LeetCodeClient,
    slug: str,
    neetcode_entry: Optional[Dict[str, Any]],
    videos: Dict[str, Any],
    force: bool,
) -> Optional[Path]:
    try:
        question = get_question(client, slug)
    except (HTTPError, URLError, ValueError, OSError) as error:
        print("Failed to fetch %s: %s" % (slug, error))
        return None
    if not question:
        print("Skipping %s: LeetCode returned no question data" % slug)
        return None
    try:
        problem_id = int(question["questionFrontendId"])
    except (KeyError, TypeError, ValueError):
        print("Skipping %s: missing frontend ID" % slug)
        return None
    title = str(question.get("title") or slug)
    notes, curated_code = load_curated(slug)
    is_premium = bool(question.get("isPaidOnly"))
    premium_description = None
    if notes and isinstance(notes.get("description"), str):
        premium_description = notes["description"].strip()
    if is_premium and not premium_description:
        print("Skipping %s: paid-only problem" % slug)
        return None
    if not is_premium and not question.get("content"):
        print("Skipping %s: problem content is null" % slug)
        return None
    topics = topic_names(question)
    pattern = problem_pattern(notes, neetcode_entry, topics)
    video_title, video_url, has_video = build_video(
        client, videos, neetcode_entry, problem_id, title
    )
    directory = migrate_problem_directory(
        problem_id, slug, str(question.get("difficulty") or "Unknown")
    )
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(
        render_problem_readme(
            question,
            pattern,
            video_title,
            video_url,
            has_video,
            notes,
            premium_description if is_premium else None,
        ),
        encoding="utf-8",
    )
    write_solution(
        directory / "solution.py",
        question,
        solution_header(question, pattern, video_url, notes),
        curated_code,
        force,
    )
    return directory


def load_question_cache(slug: str) -> Optional[Dict[str, Any]]:
    path = ROOT / ".cache" / "questions" / (slug + ".json")
    if not path.exists():
        return None
    try:
        response = json.loads(path.read_text(encoding="utf-8"))
        return response.get("data", {}).get("question")
    except (OSError, ValueError, AttributeError):
        return None


def warm_question_cache(client: LeetCodeClient) -> None:
    # A fresh clone has no .cache/, so fetch metadata the index needs.
    for path in sorted(ROOT.iterdir()):
        parsed = parse_problem_directory(path.name) if path.is_dir() else None
        if parsed is None or load_question_cache(parsed[1]) is not None:
            continue
        try:
            get_question(client, parsed[1])
        except (HTTPError, URLError, ValueError, OSError) as error:
            print("Failed to fetch %s: %s" % (parsed[1], error))


def migrate_existing_problem_directories() -> None:
    directories = [
        path
        for path in ROOT.iterdir()
        if path.is_dir() and parse_problem_directory(path.name) is not None
    ]
    for path in directories:
        parsed = parse_problem_directory(path.name)
        if parsed is None:
            continue
        problem_id, slug, unused_suffix = parsed
        del unused_suffix
        question = load_question_cache(slug)
        difficulty = str((question or {}).get("difficulty") or "").lower()
        if difficulty not in ("easy", "medium", "hard"):
            continue
        migrate_problem_directory(problem_id, slug, difficulty)


def readme_title(path: Path) -> str:
    try:
        first_line = path.read_text(encoding="utf-8").splitlines()[0]
        match = re.match(r"#\s+\d+\.\s+(.+)", first_line)
        return match.group(1).strip() if match else path.parent.name
    except (OSError, IndexError):
        return path.parent.name


def run_solutions() -> Dict[str, Tuple[str, str]]:
    statuses = {}  # type: Dict[str, Tuple[str, str]]
    for solution in sorted(ROOT.glob("*/solution.py")):
        parsed = parse_problem_directory(solution.parent.name)
        if parsed is None:
            continue
        problem_id, slug, suffix = parsed
        question = load_question_cache(slug)
        difficulty = suffix or str((question or {}).get("difficulty") or "Unknown")
        directory_name = problem_directory_name(problem_id, slug, difficulty)
        try:
            result = subprocess.run(
                [sys.executable, str(solution)],
                capture_output=True,
                text=True,
                timeout=10,
            )
            output = (result.stdout or "") + (result.stderr or "")
            if result.returncode != 0:
                status = "❌ Failing"
            elif "# STATUS: TODO" in solution.read_text(encoding="utf-8"):
                status = "⬜ Todo"
            else:
                status = "✅ Solved"
        except subprocess.TimeoutExpired as error:
            output = str(error)
            status = "❌ Failing"
        except OSError as error:
            output = str(error)
            status = "❌ Failing"
        statuses[directory_name] = (status, output)
        print("%s %s" % (status, solution.parent.name))
        if status == "❌ Failing":
            print(output.rstrip() or "(no output)")
    return statuses


def row_metadata(
    directory: Path,
    neetcode: Dict[str, Dict[str, Any]],
    videos: Dict[str, Any],
) -> Dict[str, Any]:
    parsed = parse_problem_directory(directory.name)
    if parsed is None:
        raise ValueError("Unrecognized problem directory: " + directory.name)
    problem_id, slug, directory_difficulty = parsed
    question = load_question_cache(slug) or {}
    notes, unused_code = load_curated(slug)
    del unused_code
    nc = neetcode.get(slug, {})
    tags = topic_names(question)
    pattern = problem_pattern(notes, nc, tags)
    title = str(question.get("title") or readme_title(directory / "README.md"))
    difficulty = str(question.get("difficulty") or directory_difficulty or "Unknown")
    video_id = str(nc.get("video") or "").strip()
    if video_id:
        video_url = "https://www.youtube.com/watch?v=" + video_id
        cached = videos.get(video_id)
        if isinstance(cached, dict) and cached.get("title"):
            video_title = str(cached["title"])
        else:
            video_title = "NeetCode video explanation"
        video_kind = "NeetCode"
    else:
        search_term = "leetcode %d %s neetcode" % (problem_id, title)
        video_url = (
            "https://www.youtube.com/results?"
            + urlencode({"search_query": search_term})
        )
        video_title = search_term
        video_kind = "Search"
    return {
        "id": problem_id,
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "pattern": pattern,
        "video_url": video_url,
        "video_title": video_title,
        "video_kind": video_kind,
        "premium": bool(question.get("isPaidOnly")),
    }


def rebuild_root_readme(
    statuses: Dict[str, Tuple[str, str]],
    neetcode_entries: List[Dict[str, Any]],
    videos: Dict[str, Any],
) -> None:
    nc_by_slug = neetcode_by_slug(neetcode_entries)
    directories = [
        path
        for path in ROOT.iterdir()
        if path.is_dir()
        and parse_problem_directory(path.name) is not None
        and (path / "solution.py").exists()
    ]
    rows = []
    for directory in directories:
        metadata = row_metadata(directory, nc_by_slug, videos)
        status_name = problem_directory_name(
            metadata["id"], metadata["slug"], metadata["difficulty"]
        )
        status = statuses.get(status_name, ("⬜ Todo", ""))[0]
        rows.append((metadata, status))
    rows.sort(key=lambda item: item[0]["id"])
    difficulties = {}
    for metadata, status in rows:
        count = difficulties.setdefault(
            metadata["difficulty"], {"total": 0, "solved": 0}
        )
        count["total"] += 1
        if status == "✅ Solved":
            count["solved"] += 1
    progress = "\n".join(
        "- %s: %d/%d solved"
        % (difficulty, counts["solved"], counts["total"])
        for difficulty, counts in sorted(difficulties.items())
    )
    if not progress:
        progress = "_No problems generated yet._"
    lines = [
        "# LeetCode Practice",
        "",
        "A locally generated study repo with problem statements, curated approaches, and runnable Python solutions.",
        "",
        "## Usage",
        "",
        "```sh",
        "python3 fetch_problems.py --list neetcode150",
        "python3 fetch_problems.py --list blind75 --start 0 --batch-size 20",
        "python3 fetch_problems.py --slugs two-sum,valid-anagram",
        "python3 fetch_problems.py --index-only",
        "```",
        "",
        "## Progress",
        "",
        progress,
        "",
        "## Problems",
        "",
        "| # | Title | Pattern | Difficulty | Solution | Video Guide | Status |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for metadata, status in rows:
        problem_dir = problem_directory_name(
            metadata["id"], metadata["slug"], metadata["difficulty"]
        )
        title_url = "https://leetcode.com/problems/%s/" % metadata["slug"]
        display_title = metadata["title"] + (" 🔒" if metadata["premium"] else "")
        video_icon = "▶" if metadata["video_kind"] == "NeetCode" else "🔎"
        video_label = metadata["video_kind"]
        lines.append(
            "| %d | [%s](%s) | %s | %s | [solution](./%s/solution.py) | "
            "[%s %s](%s) | %s |"
            % (
                metadata["id"],
                display_title,
                title_url,
                metadata["pattern"],
                metadata["difficulty"],
                problem_dir,
                video_icon,
                video_label,
                metadata["video_url"],
                status,
            )
        )
    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--list",
        dest="list_name",
        choices=("blind75", "neetcode150", "all"),
        default="neetcode150",
    )
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--slugs", help="Comma-separated explicit problem slugs")
    parser.add_argument("--sleep", type=float, default=1.5)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--index-only", action="store_true")
    args = parser.parse_args()
    if args.start < 0:
        parser.error("--start must be non-negative")
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")
    if args.sleep < 0:
        parser.error("--sleep must be non-negative")
    return args


def main() -> int:
    args = parse_args()
    client = LeetCodeClient(args.sleep, args.refresh)
    neetcode_entries = []  # type: List[Dict[str, Any]]
    videos = load_video_cache() if args.index_only or not args.refresh else {}
    if args.index_only:
        try:
            neetcode_entries = load_neetcode(client)
        except (HTTPError, URLError, ValueError, OSError) as error:
            print("Unable to load NeetCode data: %s" % error)
        warm_question_cache(client)
        migrate_existing_problem_directories()
    else:
        try:
            neetcode_entries = load_neetcode(client)
        except (HTTPError, URLError, ValueError, OSError) as error:
            print("Unable to load NeetCode data: %s" % error)
            return 1
        migrate_existing_problem_directories()
        try:
            selected = select_problems(args, client, neetcode_entries)
        except (HTTPError, URLError, ValueError, OSError) as error:
            print("Unable to enumerate problems: %s" % error)
            return 1
        nc_by_slug = neetcode_by_slug(neetcode_entries)
        for slug, listed_id in selected:
            if not slug:
                continue
            if listed_id is not None:
                print("Fetching %s (%04d)" % (slug, listed_id))
            else:
                print("Fetching %s" % slug)
            generate_problem(
                client, slug, nc_by_slug.get(slug), videos, args.force
            )
    save_video_cache(videos)
    statuses = run_solutions()
    rebuild_root_readme(statuses, neetcode_entries, videos)
    return 1 if any(status == "❌ Failing" for status, output in statuses.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
