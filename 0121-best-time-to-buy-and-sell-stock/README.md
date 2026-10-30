# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Tags:** Array, Dynamic Programming  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:**

```

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

**Example 2:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

```

**Constraints:**

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Video Explanation

[Sliding Window: Best Time to Buy and Sell Stock - Leetcode 121 - Python](https://www.youtube.com/watch?v=1pkOgXD63yU)

## Approach

### Intuition

For each sell day, the best earlier buy is the minimum price seen so far.

### Brute Force

Try each buy day with every later sell day and keep the greatest nonnegative profit.

### Optimal

Scan once, update the minimum price, and compare today's price against that minimum to update the best profit.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- A decreasing price sequence allows no profitable trade, so the answer stays zero.
- A single price cannot produce a transaction and yields zero.
