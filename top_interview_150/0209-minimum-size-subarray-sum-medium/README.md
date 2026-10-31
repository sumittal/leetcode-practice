# 209. Minimum Size Subarray Sum

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Sliding Window, Prefix Sum  
**Companies:** Citigroup, HCL, Bloomberg, TikTok, DoorDash, Microsoft, Amazon, Meta, Google, Oracle, Infosys, Yandex, tcs, Apple, Goldman Sachs  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a* *subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

**Example 1:**

```

**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

```

**Example 2:**

```

**Input:** target = 4, nums = [1,4,4]
**Output:** 1

```

**Example 3:**

```

**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0

```

**Constraints:**

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Video Explanation

[Minimum Size Subarray Sum - Leetcode 209 - Python](https://www.youtube.com/watch?v=aYqYMIqZx5s)

## Approach

### Intuition

With positive numbers, expanding the window increases its sum and shrinking it decreases the sum.

### Brute Force

Sum every contiguous subarray and track the shortest one reaching target.

### Optimal

Grow a sliding window until it reaches target, then shrink from the left while it remains valid.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- No window may reach target, in which case return zero.
- All values are positive, which makes window shrinking safe.
- A single value may already reach the target.
