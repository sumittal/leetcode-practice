# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium  
**Tags:** Array, Binary Search  
**Companies:** Tinkoff, Instacart, Splunk, Meta, Applied Intuition, LinkedIn, NetApp, Airtel, Apple, Bloomberg, Amazon, Capgemini, tcs, Turing, TikTok (+15 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
**Input:** nums = [5,7,7,8,8,10], target = 8
**Output:** [3,4]

```

**Example 2:**

```
**Input:** nums = [5,7,7,8,8,10], target = 6
**Output:** [-1,-1]

```

**Example 3:**

```
**Input:** nums = [], target = 0
**Output:** [-1,-1]

```

**Constraints:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Video Explanation

[First and Last Position of Element in Sorted Array - Binary Search - Leetcode 34](https://www.youtube.com/watch?v=4sQL7R5ySUU)

## Approach

### Intuition

The first and last occurrences are the lower bound of target and the lower bound of target plus one, minus one.

### Brute Force

Scan the full array and record the first and last matching positions.

### Optimal

Run two binary searches for the target's left and right boundaries.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(log n) | O(1) |

### Edge cases

- A missing target returns [-1, -1].
- A single occurrence returns the same index twice.
- Duplicates spanning the array endpoints are handled by the boundary searches.
