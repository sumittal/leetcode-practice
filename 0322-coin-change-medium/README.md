# 322. Coin Change

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/coin-change/](https://leetcode.com/problems/coin-change/)

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest** number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```

**Input:** coins = [1,2,5], amount = 11
**Output:** 3
**Explanation:** 11 = 5 + 5 + 1

```

**Example 2:**

```

**Input:** coins = [2], amount = 3
**Output:** -1

```

**Example 3:**

```

**Input:** coins = [1], amount = 0
**Output:** 0

```

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Video Explanation

[Coin Change - Dynamic Programming Bottom Up - Leetcode 322](https://www.youtube.com/watch?v=H9bfqozjoqs)

## Approach

### Intuition

The fewest coins for amount a is one plus the best result for a minus one coin denomination.

### Brute Force

Explore every coin sequence recursively.

### Optimal

Build a bottom-up minimum-coin table from amount zero through the target.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(amount) |
| Optimal | O(amount*coins) | O(amount) |

### Edge cases

- Amount zero needs zero coins.
- Unreachable totals retain an infinity sentinel and return -1.
