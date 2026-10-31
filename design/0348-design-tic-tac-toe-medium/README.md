# 348. Design Tic-Tac-Toe

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Design, Matrix, Simulation  
**Companies:** Wise, Databricks, Waymo, Citadel, Apple, Meta, Airbnb, Microsoft, Amazon, TikTok, Google, Bloomberg  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-tic-tac-toe/](https://leetcode.com/problems/design-tic-tac-toe/)

## Problem

Design a two-player game board that reports as soon as a move completes a row, column, or diagonal. Example 1: on a 3 by 3 board, moves (0,0,1), (0,2,2), (2,2,1), (1,1,2), (2,0,1), (1,0,2), and (2,1,1) make player 1 win on the final move. Example 2: on a 2 by 2 board, moves (0,0,2), (1,1,1), and (0,1,2) make player 2 win. Constraints: board size is positive and each move uses an empty cell within the board.

## Video Explanation

[YouTube search: Search YouTube for leetcode 348 Design Tic-Tac-Toe neetcode](https://www.youtube.com/results?search_query=leetcode+348+Design+Tic-Tac-Toe+neetcode)

## Approach

### Intuition

Keep signed counts for every row, column, and diagonal; a player wins when one count reaches the board size in magnitude.

### Brute Force

After each move, scan its entire row, column, and any applicable diagonals.

### Optimal

Update one row and column count and at most two diagonal counts for each move.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | move O(n), initialization O(n^2) | O(n^2) |
| Optimal | move O(1), initialization O(n) | O(n) |

### Edge cases

- A move on both diagonals updates both diagonal counters.
- After a winner is found, subsequent valid moves are not part of the game.
