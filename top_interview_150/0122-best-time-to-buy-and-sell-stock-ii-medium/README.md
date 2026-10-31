# 122. Best Time to Buy and Sell Stock II

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Greedy  
**Companies:** Careem, Toast, Nike, Sigmoid, ServiceNow, Groww, Apple, Geico, Amazon, Infosys, Meesho, Optiver, Bloomberg, eBay, Meta (+11 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the **same day**, ensuring you never hold more than one share of the stock.

Find and return *the **maximum** profit you can achieve*.

**Example 1:**

```

**Input:** prices = [7,1,5,3,6,4]
**Output:** 7
**Explanation:** Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

```

**Example 2:**

```

**Input:** prices = [1,2,3,4,5]
**Output:** 4
**Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

```

**Example 3:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

```

**Constraints:**

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Video Explanation

[Best Time to Buy and Sell a Stock II - Leetcode 122 - Python](https://www.youtube.com/watch?v=3SJ3pUkPQMc)

## Approach

### Intuition

Every profitable rising segment can be collected by buying before each increase and selling after it.

### Brute Force

Try every sequence of non-overlapping buy and sell days and retain the best total profit.

### Optimal

Sum each positive adjacent-day price difference; this equals capturing all upward runs.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A decreasing price sequence produces zero profit.
- A one-day input cannot contain a transaction.
- Flat adjacent prices add no profit.
