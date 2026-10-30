# 217. Contains Duplicate

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Sorting  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Video Explanation

[Contains Duplicate - Leetcode 217 - Python](https://www.youtube.com/watch?v=3OamzN90kPg)

## Approach

### Intuition

A duplicate exists exactly when a value is encountered a second time. A set records which values have already appeared.

### Brute Force

Compare every pair of values and return true when two are equal.

### Optimal

Insert values into a set while scanning; a value already in the set proves a duplicate.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty or one-element input has no duplicate.
- Negative values and repeated values are handled the same way as positive values.
