# 51. N-Queens

**Difficulty:** Hard  
**Tags:** Array, Backtracking, Algorithm X  
**Companies:** Mastercard, TikTok, Huawei, Zoho, Amazon, Microsoft, Google, Bloomberg, Adobe, Meta, Accenture, Oracle, Infosys, Goldman Sachs, tcs (+1 more)  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/n-queens/](https://leetcode.com/problems/n-queens/)

## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```

**Input:** n = 4
**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

```

**Example 2:**

```

**Input:** n = 1
**Output:** [["Q"]]

```

**Constraints:**

- `1 <= n <= 9`

## Video Explanation

[N-Queens - Backtracking - Leetcode 51 - Python](https://www.youtube.com/watch?v=Ph95IHmRp5M)

## Approach

### Intuition

Place one queen per row while tracking occupied columns and both diagonal directions.

### Brute Force

Try every arrangement of n queen positions and reject any pair that attacks.

### Optimal

Backtrack row by row and test column and diagonal sets before placing each queen.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n! n) | O(n) |
| Optimal | O(n!) in the common bound | O(n) besides output |

### Edge cases

- For n = 1, the board containing one queen is the sole solution.
- For n = 2 or n = 3, no valid board exists.
