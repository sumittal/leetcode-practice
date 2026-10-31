# 739. Daily Temperatures

**Difficulty:** Medium  
**Tags:** Array, Stack, Monotonic Stack  
**Companies:** Disney, Agoda, Zoho, Grab, Anduril, Chime, Swiggy, Morgan Stanley, Tekion, TikTok, josh technology, Amazon, Bloomberg, Microsoft, Intuit (+10 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/)

## Problem

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `i^th` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
**Input:** temperatures = [73,74,75,71,69,72,76,73]
**Output:** [1,1,4,2,1,1,0,0]

```

**Example 2:**

```
**Input:** temperatures = [30,40,50,60]
**Output:** [1,1,1,0]

```

**Example 3:**

```
**Input:** temperatures = [30,60,90]
**Output:** [1,1,0]

```

**Constraints:**

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Video Explanation

[Daily Temperatures - Monotonic Stack - Leetcode 739 - Python](https://www.youtube.com/watch?v=cTBiBSnjO3c)

## Approach

### Intuition

A warmer day resolves earlier days whose temperatures are lower.

### Brute Force

For every day, scan forward to find the first higher temperature.

### Optimal

Maintain indices of unresolved days in a decreasing-temperature stack.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) besides the output |
| Optimal | O(n) | O(n) |

### Edge cases

- A day with no warmer future day receives zero.
- Equal temperatures do not resolve one another.
