# 312. Burst Balloons

**Difficulty:** Hard  
**Tags:** Array, Dynamic Programming  
**Companies:** Samsung, Snap, UiPath, PhonePe, Paytm, tcs, Uber, Google, Infosys, Amazon, Cisco, Microsoft, Salesforce, Bloomberg, Goldman Sachs (+1 more)  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/burst-balloons/](https://leetcode.com/problems/burst-balloons/)

## Problem

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `i^th` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return *the maximum coins you can collect by bursting the balloons wisely*.

**Example 1:**

```

**Input:** nums = [3,1,5,8]
**Output:** 167
**Explanation:**
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

**Example 2:**

```

**Input:** nums = [1,5]
**Output:** 10

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`

## Video Explanation

[Burst Baloons - Dynamic Programming - Leetcode 312 - Python](https://www.youtube.com/watch?v=VFskby7lUbw)

## Approach

### Intuition

For an interval, choose which balloon is popped last; its neighbors are then fixed interval boundaries.

### Brute Force

Try every possible next balloon to pop and recursively solve the remaining array.

### Optimal

Pad the array with boundary ones and use interval DP, selecting the last balloon popped between each pair of boundaries.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n!) | O(n) |
| Optimal | O(n^3) | O(n^2) |

### Edge cases

- No balloons yields zero coins.
- The padded boundary balloons are never burst.
