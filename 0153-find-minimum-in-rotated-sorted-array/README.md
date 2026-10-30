# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium  
**Tags:** Array, Binary Search  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time`.

**Example 1:**

```

**Input:** nums = [3,4,5,1,2]
**Output:** 1
**Explanation:** The original array was [1,2,3,4,5] rotated 3 times.

```

**Example 2:**

```

**Input:** nums = [4,5,6,7,0,1,2]
**Output:** 0
**Explanation:** The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

```

**Example 3:**

```

**Input:** nums = [11,13,15,17]
**Output:** 11
**Explanation:** The original array was [11,13,15,17] and it was rotated 4 times.

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Video Explanation

[Find Minimum in Rotated Sorted Array - Binary Search - Leetcode 153 - Python](https://www.youtube.com/watch?v=nIVW4P8b1VA)

## Approach

### Intuition

The rotation pivot separates two sorted ranges; comparing the midpoint with the right endpoint identifies which range contains the minimum.

### Brute Force

Scan the array and return its smallest value.

### Optimal

Binary search while maintaining a range containing the minimum. If mid is larger than right, discard the left half through mid; otherwise keep mid and discard the right side.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(log n) | O(1) |

### Edge cases

- A one-element array is already its own minimum.
- An unrotated array repeatedly keeps the left half until its first element remains.
- Do not discard mid when nums[mid] may itself be the minimum.
