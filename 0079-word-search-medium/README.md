# 79. Word Search

**Difficulty:** Medium  
**Tags:** Array, String, Backtracking, Depth-First Search, Matrix  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/word-search/](https://leetcode.com/problems/word-search/)

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
**Output:** true

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
**Output:** false

```

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## Video Explanation

[Word Search - Backtracking - Leetcode 79 - Python](https://www.youtube.com/watch?v=pfiQ_PS1g8E)

## Approach

### Intuition

The word must follow adjacent board cells without reusing a cell in its path.

### Brute Force

Try every possible path without pruning by matching prefix.

### Optimal

DFS only along matching next letters and mark/unmark the current cell.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(R*C*4^L) | O(L) |
| Optimal | O(R*C*3^L) | O(L) |

### Edge cases

- A one-letter word matches any equal cell.
- Restore visited cells on every return path.
