"""
LeetCode 68: Text Justification
Difficulty: Hard
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=TzMl4Z7pVh8
Complexity:
    - Time: O(total characters)
    - Space: O(total output)
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Each outer iteration selects the next maximal fitting word group.
        result = []
        first = 0
        while first < len(words):
            last = first
            letters = 0
            # Reserve one space between each adjacent pair while packing words.
            while last < len(words) and (
                letters + len(words[last]) + (last - first) <= maxWidth
            ):
                letters += len(words[last])
                last += 1
            gaps = last - first - 1
            line_words = words[first:last]
            # The final line and single-word lines use left justification.
            if last == len(words) or gaps == 0:
                line = " ".join(line_words).ljust(maxWidth)
            else:
                # Divide all required spaces evenly across the available gaps.
                spaces, extra = divmod(maxWidth - letters, gaps)
                pieces = []
                for gap in range(gaps):
                    pieces.append(line_words[gap])
                    # Remainder spaces are assigned to the leftmost gaps first.
                    pieces.append(" " * (spaces + (1 if gap < extra else 0)))
                pieces.append(line_words[-1])
                line = "".join(pieces)
            # Every emitted line has exactly maxWidth characters.
            result.append(line)
            # Advancing first consumes each word in exactly one line.
            first = last
        # Joining line words is linear in the total rendered output.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == ["This    is    an", "example  of text", "justification.  "]
    assert solution.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16
    ) == ["What   must   be", "acknowledgment  ", "shall be        "]
    assert solution.fullJustify(
        [
            "Science", "is", "what", "we", "understand", "well", "enough",
            "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
            "else", "we", "do",
        ],
        20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
    assert solution.fullJustify(["Single"], 8) == ["Single  "]
    print("All tests passed")
