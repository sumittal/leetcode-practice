# 35. Search Insert Position

**Difficulty:** Easy  
**Tags:** Array, Binary Search  
**Companies:** Grammarly, Bloomberg, Microsoft, Amazon, Google, Accenture, Meta, tcs, Zoho, Infosys, Yandex  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```

**Input:** nums = [1,3,5,6], target = 5
**Output:** 2

```

**Example 2:**

```

**Input:** nums = [1,3,5,6], target = 2
**Output:** 1

```

**Example 3:**

```

**Input:** nums = [1,3,5,6], target = 7
**Output:** 4

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Video Explanation

[Search Insert Position - Binary Search - Leetcode 35 - Python](https://www.youtube.com/watch?v=K-RYzDZkzCI)

## Approach

### Intuition

The insertion index is the first position whose value is not smaller than the target.

### Brute Force

Scan from the beginning until reaching a value at least as large as the target.

### Optimal

Binary-search the lower bound in the sorted array.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(log n) | O(1) |

### Edge cases

- A target below all values returns index zero.
- A target above all values returns the array length.
- An existing target returns its index.
