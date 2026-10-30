"""
LeetCode 79: Word Search
Difficulty: Medium
Pattern: Backtracking
Video Reference: https://www.youtube.com/watch?v=pfiQ_PS1g8E
Complexity:
    - Time: O(R*C*3^L)
    - Space: O(L)
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Recursive indices identify the next required letter after the current prefix.
        rows = len(board)
        cols = len(board[0]) if rows else 0

        def search(r: int, c: int, index: int) -> bool:
            # Reaching the word length means every requested character matched.
            if index == len(word):
                return True
            # Bounds and mismatch checks happen before indexing or marking the cell.
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[index]:
                return False
            char = board[r][c]
            board[r][c] = "!"  # Mark this cell for this path only.
            # A neighbor advances exactly one character; the marker prevents revisiting.
            found = any(
                search(r + dr, c + dc, index + 1)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
            board[r][c] = (
                char  # Restore even after a successful branch for caller safety.
            )
            # The return value says whether any allowed neighbor completed the suffix.
            return found

        # Any starting cell may begin the word; a failed start leaves the board restored.
        return any(search(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    solution = Solution()
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solution.exist(b, "ABCCED") is True
    assert solution.exist(b, "SEE") is True
    assert solution.exist(b, "ABCB") is False
    assert solution.exist([["a"]], "a") is True
    assert solution.exist([["a"]], "aa") is False
    print("All tests passed")
