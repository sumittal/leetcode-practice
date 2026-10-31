# 371. Sum of Two Integers

**Difficulty:** Medium  
**Tags:** Math, Bit Manipulation  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/sum-of-two-integers/](https://leetcode.com/problems/sum-of-two-integers/)

## Problem

Given two integers `a` and `b`, return *the sum of the two integers without using the operators* `+` *and* `-`.

**Example 1:**

```
**Input:** a = 1, b = 2
**Output:** 3

```

**Example 2:**

```
**Input:** a = 2, b = 3
**Output:** 5

```

**Constraints:**

- `-1000 <= a, b <= 1000`

## Video Explanation

[Sum of Two Integers - Leetcode 371 - Java](https://www.youtube.com/watch?v=gVUrDV4tZfY)

## Approach

### Intuition

XOR adds bits without carry; AND shifted left identifies carry bits to add next.

### Brute Force

Use arithmetic addition directly.

### Optimal

Iterate masked XOR and shifted carry until carry is zero, then convert the 32-bit result to signed form.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(1) | O(1) |
| Optimal | O(1) | O(1) |

### Edge cases

- Mask every intermediate because Python integers have arbitrary precision and negative values are unbounded.
- Convert values with the sign bit set back to negative signed-32-bit form.
