"""
LeetCode 212: Word Search II
Difficulty: Hard
Pattern: Tries
Video Reference: https://www.youtube.com/watch?v=asbcE9mZz_U
Complexity:
    - Time: O(R*C*4^L) worst case
    - Space: O(total word chars + R*C)
"""

from typing import Any, Dict, List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Every trie terminal stores the full matching word for O(1) reporting.
        root = {}
        for word in words:
            node = root
            # Prefix paths are shared, reducing repeated board exploration.
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = word
        rows = len(board)
        cols = len(board[0]) if rows else 0
        found = set()

        def dfs(r: int, c: int, parent: Dict[str, Any]) -> None:
            # parent is the trie node for the prefix matched before this board cell.
            char = board[r][c]
            if char not in parent:
                return
            node = parent[char]
            # A terminal stores its full word so traversal can report it directly.
            if "#" in node:
                found.add(node.pop("#"))  # Remove terminal to avoid duplicate paths.
            board[r][c] = "!"  # Mark the cell so one path cannot reuse it.
            # Explore only neighbors that can extend the current trie prefix.
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "!":
                    dfs(nr, nc, node)
            # Restore the board so other words and starting paths see the original cell.
            board[r][c] = char
            if not node:
                parent.pop(char)  # Prune exhausted prefixes from future searches.

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(found)


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert sorted(solution.findWords(board, ["oath", "pea", "eat", "rain"])) == [
        "eat",
        "oath",
    ]
    assert solution.findWords([["a", "b"], ["c", "d"]], ["abcb"]) == []
    assert solution.findWords([["a"]], ["a", "a"]) == ["a"]
    print("All tests passed")
