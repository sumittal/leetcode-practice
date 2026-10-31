# 215. Kth Largest Element in an Array

**Difficulty:** Medium  
**Tags:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect  
**Pattern:** Heap / Priority Queue  
**LeetCode:** [https://leetcode.com/problems/kth-largest-element-in-an-array/](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem

Given an integer array `nums` and an integer `k`, return *the* `k^th` *largest element in the array*.

Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.

Can you solve it without sorting?

**Example 1:**

```
**Input:** nums = [3,2,1,5,6,4], k = 2
**Output:** 5

```

**Example 2:**

```
**Input:** nums = [3,2,3,1,2,4,5,5,6], k = 4
**Output:** 4

```

**Constraints:**

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Video Explanation

[Kth Largest Element in an Array - Quick Select - Leetcode 215 - Python](https://www.youtube.com/watch?v=XEmy13g1Qxc)

## Approach

### Intuition

The kth-largest value is the minimum among the largest k values.

### Brute Force

Sort the array and read the value k positions from the end.

### Optimal

Maintain a size-k min-heap while scanning the array; a heap gives O(n log k) worst-case time. Quickselect is O(n) on average but O(n^2) in the worst case.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(1) or O(n), depending on the sort |
| Optimal | O(n log k) worst case | O(k) |

### Edge cases

- k may equal the array length, making the answer the minimum.
- Duplicate values count as separate elements.
