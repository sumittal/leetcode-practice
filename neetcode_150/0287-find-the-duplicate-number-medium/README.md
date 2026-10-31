# 287. Find the Duplicate Number

**Difficulty:** Medium  
**Tags:** Array, Two Pointers, Binary Search, Bit Manipulation, Pigeonhole Principle, Floyd's Cycle Finding Algorithm  
**Companies:** Nike, DP world, Citadel, Nvidia, Amazon, Walmart Labs, Bloomberg, Anduril, Microsoft, Google, Flipkart, Zoho, tcs, Meta, Cisco (+3 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/find-the-duplicate-number/](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

**Example 1:**

```

**Input:** nums = [1,3,4,2,2]
**Output:** 2

```

**Example 2:**

```

**Input:** nums = [3,1,3,4,2]
**Output:** 3

```

**Example 3:**

```

**Input:** nums = [3,3,3,3,3]
**Output:** 3
```

**Constraints:**

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

**Follow up:**

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

## Video Explanation

[Find the Duplicate Number - Floyd's Cycle Detection - Leetcode 287 - Python](https://www.youtube.com/watch?v=wjYnzkAhcNk)

## Approach

### Intuition

Treat each value as the next array index; the duplicate creates a cycle in this index graph.

### Brute Force

Compare each value with the rest of the array to find a repeated value.

### Optimal

Use Floyd's slow and fast pointers to find the cycle intersection, then locate the cycle entrance.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- The duplicate can occur more than twice.
- The input array must remain unmodified.
