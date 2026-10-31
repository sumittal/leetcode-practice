# 42. Trapping Rain Water

**Difficulty:** Hard  
**Tags:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack  
**Companies:** Goldman Sachs, Zenefits, Rakuten, ThousandEyes, X, Zoho, Walmart Labs, Samsung, Urban Company, ServiceNow, Amazon, Tekion, Wix, Hive, Sigmoid (+55 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**Output:** 6
**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

```

**Input:** height = [4,2,0,3,2,5]
**Output:** 9

```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Video Explanation

[Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)

## Approach

### Intuition

Water above a bar is limited by the shorter of the tallest walls on its left and right.

### Brute Force

For each index, scan both sides for their maximum heights and add the trapped depth.

### Optimal

Move inward from both ends while tracking the maximum wall seen on each side; the shorter side determines safe water.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- Fewer than three bars trap no water.
- A monotone height profile traps no water.
