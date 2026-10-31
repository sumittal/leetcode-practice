# 33. Search in Rotated Sorted Array

**Difficulty:** Medium  
**Tags:** Array, Binary Search  
**Companies:** Cohesity, Delhivery, Tinkoff, Grammarly, Autodesk, Walmart Labs, FreshWorks, Arista Networks, Criteo, Nvidia, TikTok, Amazon, Paytm, Zoho, Oracle (+30 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target`* if it is in* `nums`*, or* `-1`* if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

```

**Example 2:**

```
**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1

```

**Example 3:**

```
**Input:** nums = [1], target = 0
**Output:** -1

```

**Constraints:**

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Video Explanation

[Search in rotated sorted array - Leetcode 33 - Python](https://www.youtube.com/watch?v=U8XENwh8Oy8)

## Approach

### Intuition

At least one half of a rotated, distinct sorted array is ordered; determine whether the target lies in that half.

### Brute Force

Scan all values and return the index of the target when found.

### Optimal

Binary search. Identify the sorted half, keep it only if the target is within its inclusive bounds, and otherwise search the other half.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(log n) | O(1) |

### Edge cases

- A one-element array can match at index zero or return -1.
- Use inclusive range checks so targets at either endpoint remain searchable.
- When the target is absent, each iteration must still discard at least one index.
