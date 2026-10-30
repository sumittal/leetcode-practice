# 347. Top K Frequent Elements

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Video Explanation

[Top K Frequent Elements - Bucket Sort - Leetcode 347 - Python](https://www.youtube.com/watch?v=YPTqKIgVk-k)

## Approach

### Intuition

Count each value once, then select the values with the greatest frequencies.

### Brute Force

Count values and repeatedly scan the remaining counts to select the next most frequent value.

### Optimal

Bucket values by frequency and scan buckets from highest frequency down until k values are collected. A heap is an alternative with O(n log k) time.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nk) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- When k equals the number of distinct values, return each distinct value once.
- Ties in frequency may be returned in any order.
