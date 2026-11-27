import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import fetch_problems as fetch


class StudyIndexesTest(unittest.TestCase):
    def setUp(self):
        repo = TemporaryDirectory()
        self.addCleanup(repo.cleanup)
        self.root = Path(repo.name)
        root_patch = patch.object(fetch, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        quiet = redirect_stdout(io.StringIO())
        quiet.__enter__()
        self.addCleanup(quiet.__exit__, None, None, None)

    def run_fetch(self, *args):
        with patch.object(sys, "argv", ["fetch_problems.py", *args]):
            self.assertEqual(fetch.main(), 0)

    def test_fetch_places_problem_and_updates_both_indexes(self):
        question = {
            "questionFrontendId": "1234",
            "titleSlug": "study-example",
            "title": "Study Example",
            "difficulty": "Medium",
            "content": "<p>Example problem.</p>",
            "topicTags": [{"name": "Hash Table"}],
        }
        with (
            patch.object(fetch, "load_study_plan", return_value=[]),
            patch.object(fetch, "load_company_data", return_value={}),
            patch.object(fetch, "load_design_list", return_value=[question]),
            patch.object(fetch, "load_neetcode", return_value=[]) as load_neetcode,
            patch.object(fetch, "get_question", return_value=question),
        ):
            self.run_fetch("--slugs", "study-example")
            old_topic = self.root / "problems" / "design"
            original = old_topic / "1234-study-example-medium"
            solution = b"class Solution:\n    pass\n"
            (original / "solution.py").write_bytes(solution)
            self.assertIn("## Medium", (old_topic / "README.md").read_text())
            self.assertIn("# Design", (old_topic / "README.md").read_text())
            self.assertIn("LeetCode Design extra", (original / "README.md").read_text())
            self.assertIn("[Design](../problems/design/README.md)", self.index("medium"))

            load_neetcode.return_value = [
                {"link": "/problems/study-example/", "neetcode150": True, "pattern": "Trees"}
            ]
            question["difficulty"] = "Hard"
            self.run_fetch("--slugs", "study-example")

        new_topic = self.root / "problems" / "trees"
        relocated = new_topic / "1234-study-example-hard"
        self.assertEqual((relocated / "solution.py").read_bytes(), solution)
        self.assertFalse(original.exists())
        self.assertFalse((old_topic / "README.md").exists())
        self.assertIn("## Hard", (new_topic / "README.md").read_text())
        self.assertIn("1234-study-example-hard/README.md", self.index("hard"))
        self.assertNotIn("study-example", self.index("medium"))

    def index(self, difficulty):
        return (self.root / "by_difficulty" / (difficulty + ".md")).read_text()

    def test_index_only_uses_local_problem_files_without_fetching(self):
        problem = self.root / "problems" / "binary-search" / "1234-study-example-easy"
        problem.mkdir(parents=True)
        (problem / "README.md").write_text(
            "# 1234. Study Example\n\n**Pattern:** Binary Search  \n"
            "**Study list:** Blind 75  \n",
            encoding="utf-8",
        )
        (problem / "solution.py").write_text("", encoding="utf-8")
        with patch.object(fetch, "LeetCodeClient", side_effect=AssertionError("network")):
            self.run_fetch("--index-only")

        self.assertIn(
            "| [Binary Search](problems/binary-search/README.md) | 1 | 0 | 0 | 1 |",
            (self.root / "README.md").read_text(),
        )
        self.assertIn(
            "[Study Example](1234-study-example-easy/README.md)",
            (problem.parent / "README.md").read_text(),
        )
        self.assertIn(
            "[Study Example](../problems/binary-search/1234-study-example-easy/README.md)",
            self.index("easy"),
        )
        self.assertIn("Blind 75", self.index("easy"))
        self.assertFalse((self.root / ".cache").exists())

    def test_legacy_solution_is_indexed_and_preserved_on_refetch(self):
        name = "1234-study-example-easy"
        legacy = self.root / "blind_75" / name
        legacy.mkdir(parents=True)
        (legacy / "README.md").write_text(
            "# 1234. Study Example\n\n**Pattern:** Binary Search\n",
            encoding="utf-8",
        )
        solution = b"print('local solution ran')\n"
        (legacy / "solution.py").write_bytes(solution)
        self.run_fetch("--index-only")

        topic = self.root / "problems" / "binary-search"
        self.assertIn(
            f"../../blind_75/{name}/solution.py", (topic / "README.md").read_text()
        )
        self.assertIn(f"../blind_75/{name}/solution.py", self.index("easy"))
        self.assertIn("Blind 75", self.index("easy"))
        self.assertIn("✅ Solved", self.index("easy"))

        question = {
            "questionFrontendId": "1234",
            "titleSlug": "study-example",
            "title": "Study Example",
            "difficulty": "Easy",
            "content": "<p>Example problem.</p>",
            "topicTags": [{"name": "Binary Search"}],
        }
        with (
            patch.object(fetch, "load_study_plan", return_value=[]),
            patch.object(fetch, "load_company_data", return_value={}),
            patch.object(fetch, "load_design_list", return_value=[]),
            patch.object(fetch, "load_neetcode", return_value=[]),
            patch.object(fetch, "get_question", return_value=question),
        ):
            self.run_fetch("--slugs", "study-example")

        self.assertFalse(legacy.exists())
        self.assertEqual((topic / name / "solution.py").read_bytes(), solution)
        self.assertIn(f"../problems/binary-search/{name}/solution.py", self.index("easy"))

        (legacy / "__pycache__").mkdir(parents=True)
        orphan = self.root / "blind_75" / "4321-orphan-easy"
        (orphan / "__pycache__").mkdir(parents=True)
        duplicate = self.root / "neetcode_150" / "1234-study-example-medium"
        duplicate.mkdir(parents=True)
        (duplicate / "solution.py").write_text("raise AssertionError('stale copy')\n")
        self.run_fetch("--index-only")

        self.assertEqual(self.index("easy").count("| 1234 |"), 1)
        self.assertNotIn("4321", self.index("easy"))
        self.assertNotIn("1234", self.index("medium"))
        self.assertTrue((legacy / "__pycache__").is_dir())
        self.assertTrue((duplicate / "solution.py").is_file())
