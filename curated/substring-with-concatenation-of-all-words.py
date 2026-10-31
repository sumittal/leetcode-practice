from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0]:
            return []
        # Every word has equal width, so only word-aligned starts can match.
        width = len(words[0])
        word_count = len(words)
        required = Counter(words)
        matches = []
        for offset in range(width):
            left = offset
            seen = Counter()
            used = 0
            # Advancing by width keeps each candidate chunk aligned.
            for right in range(offset, len(s) - width + 1, width):
                word = s[right : right + width]
                if word not in required:
                    # A foreign chunk breaks the current concatenation window.
                    seen.clear()
                    used = 0
                    left = right + width
                    continue
                seen[word] += 1
                used += 1
                # Remove left chunks until this word fits its required multiplicity.
                while seen[word] > required[word]:
                    removed = s[left : left + width]
                    seen[removed] -= 1
                    used -= 1
                    left += width
                # A full-width match consumes exactly the requested word count.
                if used == word_count:
                    matches.append(left)
                    # Drop one leading word so overlapping matches remain possible.
                    removed = s[left : left + width]
                    seen[removed] -= 1
                    used -= 1
                    left += width
            # Each offset handles a disjoint alignment of possible starts.
        # Sorting combines offsets into increasing index order.
        return sorted(matches)


if __name__ == "__main__":
    solution = Solution()
    assert solution.findSubstring(
        "barfoothefoobarman", ["foo", "bar"]
    ) == [0, 9]
    assert solution.findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
    ) == [8]
    assert solution.findSubstring(
        "barfoofoobarthefoobarman", ["bar", "foo", "the"]
    ) == [6, 9, 12]
    assert solution.findSubstring("anything", []) == []
    print("All tests passed")
