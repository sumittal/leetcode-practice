# 309. Best Time to Buy and Sell Stock with Cooldown

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**

```

**Input:** prices = [1,2,3,0,2]
**Output:** 3
**Explanation:** transactions = [buy, sell, cooldown, buy, sell]

```

**Example 2:**

```

**Input:** prices = [1]
**Output:** 0

```

**Constraints:**

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Video Explanation

[Best Time to Buy and Sell Stock with Cooldown - Leetcode 309 - Python](https://www.youtube.com/watch?v=I7j0F7AHpb8)

## Approach

### Intuition

The best future choice depends on whether the previous day ended holding, sold, or resting.

### Brute Force

Recursively choose to buy, sell, or wait while tracking whether a cooldown day is required.

### Optimal

Track hold, sold, and rest profits with constant-size rolling state; only rest may transition to buying.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(3^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- One price provides no completed transaction.
- After selling, the next day must pass before another purchase.
