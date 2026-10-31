# 188. Best Time to Buy and Sell Stock IV

**Difficulty:** Hard  
**Tags:** Array, Dynamic Programming  
**Companies:** PubMatic, HashedIn, Citadel, Visa, Goldman Sachs, TikTok, Infosys, Apple, Google, Amazon, Microsoft, Meta  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**

```

**Input:** k = 2, prices = [2,4,1]
**Output:** 2
**Explanation:** Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

```

**Example 2:**

```

**Input:** k = 2, prices = [3,2,6,5,0,3]
**Output:** 7
**Explanation:** Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

```

**Constraints:**

- `1 <= k <= 100`
- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 1000`

## Video Explanation

[YouTube search: Search YouTube for leetcode 188 Best Time to Buy and Sell Stock IV neetcode](https://www.youtube.com/results?search_query=leetcode+188+Best+Time+to+Buy+and+Sell+Stock+IV+neetcode)

## Approach

### Intuition

For each transaction count, keep the best cash balance after buying and after selling.

### Brute Force

Enumerate up to k nonoverlapping buy-sell intervals and maximize their total profit.

### Optimal

Update buy and sell DP states for each transaction; when k is at least n/2, sum all positive daily gains.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(k) |
| Optimal | O(n k), or O(n) in the unlimited-transactions case | O(k) |

### Edge cases

- Zero transactions or fewer than two prices yield zero.
- When k >= n/2, every profitable rising segment can be captured.
- A decreasing sequence remains at zero profit.
