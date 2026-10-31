# 494. Target Sum

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Backtracking, Knapsack Problem, 0-1 Knapsack  
**Companies:** Myntra, Pinterest, Nuro, ServiceNow, Meta, Amazon, Google, Microsoft, Bloomberg  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)

## Problem

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

**Example 1:**

```

**Input:** nums = [1,1,1,1,1], target = 3
**Output:** 5
**Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

```

**Example 2:**

```

**Input:** nums = [1], target = 1
**Output:** 1

```

**Constraints:**

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Video Explanation

[Target Sum - Dynamic Programming - Leetcode 494 - Python](https://www.youtube.com/watch?v=g0npyaQtAQM)

## Approach

### Intuition

Choosing plus or minus signs is equivalent to choosing a subset with a derived target sum.

### Brute Force

Recursively assign either sign to every number and count assignments reaching the target.

### Optimal

Convert to subset sum (total + target) / 2 and count subsets with a one-dimensional DP updated downward.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n * total) | O(total) |

### Edge cases

- A target outside the absolute total or with incompatible parity has zero assignments.
- A zero-valued element doubles every existing assignment count.
