# 189. Rotate Array

**Difficulty:** Medium  
**Tags:** Array, Math, Two Pointers  
**Companies:** Fiverr, Box, Apple, EPAM Systems, Accenture, Virtusa, tcs, Siemens, razorpay, Bloomberg, Microsoft, Capgemini, Nutanix, Amazon, Google (+10 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```

**Input:** nums = [1,2,3,4,5,6,7], k = 3
**Output:** [5,6,7,1,2,3,4]
**Explanation:**
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

**Example 2:**

```

**Input:** nums = [-1,-100,3,99], k = 2
**Output:** [3,99,-1,-100]
**Explanation:**
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**Follow up:**

- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

## Video Explanation

[Rotate Array - Leetcode 189 - Python](https://www.youtube.com/watch?v=BHr381Guz3Y)

## Approach

### Intuition

A right rotation moves a suffix to the front while preserving the order inside both parts.

### Brute Force

Repeat k times: save the last value, shift all other values right, and place it first.

### Optimal

Reverse the whole array, then reverse the first k values and the remaining suffix.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nk) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- Reduce k modulo the array length.
- A zero rotation leaves the array unchanged.
- An empty array requires no mutation.
