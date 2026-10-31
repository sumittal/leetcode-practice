# 7. Reverse Integer

**Difficulty:** Medium  
**Tags:** Math  
**Companies:** Accenture, Bloomberg, tcs, Google, Apple, Amazon, Microsoft, EPAM Systems, Cognizant, Meta, Capgemini, Infosys, Oracle, LinkedIn  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/reverse-integer/](https://leetcode.com/problems/reverse-integer/)

## Problem

Given a signed 32-bit integer `x`, return `x`* with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

```

**Input:** x = 123
**Output:** 321

```

**Example 2:**

```

**Input:** x = -123
**Output:** -321

```

**Example 3:**

```

**Input:** x = 120
**Output:** 21

```

**Constraints:**

- `-2^31 <= x <= 2^31 - 1`

## Video Explanation

[Reverse Integer - Bit Manipulation - Leetcode 7 - Python](https://www.youtube.com/watch?v=HAgLH58IgJQ)

## Approach

### Intuition

Build the reversed magnitude digit by digit, then apply the original sign and check the required 32-bit range.

### Brute Force

Reverse the decimal string representation and parse it as a signed integer.

### Optimal

Extract digits arithmetically and return zero if the signed result lies outside the 32-bit range.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(log |x|) | O(log |x|) |
| Optimal | O(log |x|) | O(1) |

### Edge cases

- Trailing zeroes become leading zeroes and disappear from the result.
- Either positive or negative overflow returns zero.
