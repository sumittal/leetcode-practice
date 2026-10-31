# 416. Partition Equal Subset Sum

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/partition-equal-subset-sum/](https://leetcode.com/problems/partition-equal-subset-sum/)

## Problem

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or* `false`* otherwise*.

**Example 1:**

```

**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].

```

**Example 2:**

```

**Input:** nums = [1,2,3,5]
**Output:** false
**Explanation:** The array cannot be partitioned into equal sum subsets.

```

**Constraints:**

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Video Explanation

[Partition Equal Subset Sum - Dynamic Programming - Leetcode 416 - Python](https://www.youtube.com/watch?v=IsvocB5BJhw)

## Approach

### Intuition

Two equal-sum groups exist exactly when some subset totals half of the array sum.

### Brute Force

Enumerate all subsets and test whether any reaches half the total.

### Optimal

Use a one-dimensional subset-sum table and scan sums downward so each number is used at most once.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n * target) | O(target) |

### Edge cases

- An odd total cannot be divided into equal integer sums.
- A value larger than half the total cannot be part of a target-sum subset.
