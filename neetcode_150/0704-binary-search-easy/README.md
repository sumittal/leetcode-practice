# 704. Binary Search

**Difficulty:** Easy  
**Tags:** Array, Binary Search  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)

## Problem

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```

**Input:** nums = [-1,0,3,5,9,12], target = 9
**Output:** 4
**Explanation:** 9 exists in nums and its index is 4

```

**Example 2:**

```

**Input:** nums = [-1,0,3,5,9,12], target = 2
**Output:** -1
**Explanation:** 2 does not exist in nums so return -1

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Video Explanation

[Binary Search - Leetcode 704 - Python](https://www.youtube.com/watch?v=s4DPM8ct1pI)

## Approach

### Intuition

Sorted order lets each comparison discard half of the remaining indices.

### Brute Force

Scan the array until the target is found.

### Optimal

Binary search an inclusive interval and return -1 when it becomes empty.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(log n) | O(1) |

### Edge cases

- An empty array returns -1.
- The target may be the only element.
