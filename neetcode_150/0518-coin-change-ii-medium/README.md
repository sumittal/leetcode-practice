# 518. Coin Change II

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Knapsack Problem, Complete Knapsack  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/coin-change-ii/](https://leetcode.com/problems/coin-change-ii/)

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The **final** answer is **guaranteed** to fit into a signed **32-bit** integer.

**Example 1:**

```

**Input:** amount = 5, coins = [1,2,5]
**Output:** 4
**Explanation:** there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

```

**Example 2:**

```

**Input:** amount = 3, coins = [2]
**Output:** 0
**Explanation:** the amount of 3 cannot be made up just with coins of 2.

```

**Example 3:**

```

**Input:** amount = 10, coins = [10]
**Output:** 1

```

**Constraints:**

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- All the values of `coins` are **unique**.
- `0 <= amount <= 5000`

## Video Explanation

[Coin Change 2 - Dynamic Programming Unbounded Knapsack - Leetcode 518 - Python](https://www.youtube.com/watch?v=Mjy4hd2xgrs)

## Approach

### Intuition

Process denominations one at a time so each partial count represents combinations, not orderings.

### Brute Force

Recursively choose how many coins of each denomination contribute to the amount.

### Optimal

Use a one-dimensional ways table; iterate totals upward so the current coin can be reused, with coins as the outer loop to avoid permutation duplicates.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(amount) |
| Optimal | O(amount * number of coins) | O(amount) |

### Edge cases

- Amount zero has one combination: choose no coins.
- An unreachable positive amount has zero combinations.
