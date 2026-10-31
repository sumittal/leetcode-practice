# 212. Word Search II

**Difficulty:** Hard  
**Tags:** Array, String, Backtracking, Trie, Matrix  
**Companies:** Snowflake, Cisco, Two Sigma, Zoom, Uber, Airbnb, Aurora, TikTok, Snap, Wix, Amazon, Microsoft, DoorDash, Visa, Oracle (+4 more)  
**Pattern:** Tries  
**LeetCode:** [https://leetcode.com/problems/word-search-ii/](https://leetcode.com/problems/word-search-ii/)

## Problem

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```

**Input:** board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
**Output:** ["eat","oath"]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```

**Input:** board = [["a","b"],["c","d"]], words = ["abcb"]
**Output:** []

```

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

## Video Explanation

[Word Search II - Backtracking Trie - Leetcode 212 - Python](https://www.youtube.com/watch?v=asbcE9mZz_U)

## Approach

### Intuition

A trie shares prefixes across candidate words, and board DFS explores only prefixes that can still form a word.

### Brute Force

Run a full board search independently for every word.

### Optimal

Build a trie, DFS from each cell, mark visited cells, and remove found words/empty trie branches for pruning.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(W*R*C*4^L) | O(L) |
| Optimal | O(R*C*4^L) worst case | O(total word chars + R*C) |

### Edge cases

- A cell cannot be reused within one path.
- Remove a found terminal to avoid duplicate output.
