# 84. Largest Rectangle in Histogram

**Difficulty:** Hard  
**Tags:** Array, Stack, Monotonic Stack, Range Minimum/Maximum Query  
**Companies:** thoughtspot, Coupang, Myntra, Visa, Flipkart, BitGo, Capital One, Amazon, Waymo, Microsoft, Google, tcs, Bloomberg, Accenture, Walmart Labs (+13 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/largest-rectangle-in-histogram/](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```

**Input:** heights = [2,1,5,6,2,3]
**Output:** 10
**Explanation:** The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```

**Input:** heights = [2,4]
**Output:** 4

```

**Constraints:**

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Video Explanation

[LARGEST RECTANGLE IN HISTOGRAM - Leetcode 84 - Python](https://www.youtube.com/watch?v=zx5Sw9130L0)

## Approach

### Intuition

Each bar's widest rectangle ends at the first shorter bar on either side.

### Brute Force

For every interval, track its minimum height and calculate its area.

### Optimal

Use a monotonic increasing stack of indices; when a shorter bar arrives, pop bars and finalize their maximal widths.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty histogram has area zero.
- Equal-height bars must be combined to obtain their full width.
