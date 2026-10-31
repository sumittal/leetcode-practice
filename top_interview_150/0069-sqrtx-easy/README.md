# 69. Sqrt(x)

**Difficulty:** Easy  
**Tags:** Math, Binary Search, Newton's Method  
**Companies:** Grammarly, Zoho, TikTok, Citadel, Bloomberg, Amazon, Google, Apple, tcs, Meta, Microsoft, Adobe, LinkedIn, Goldman Sachs, Oracle (+1 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/sqrtx/](https://leetcode.com/problems/sqrtx/)

## Problem

Given a non-negative integer `x`, return *the square root of* `x`* rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

**Example 1:**

```

**Input:** x = 4
**Output:** 2
**Explanation:** The square root of 4 is 2, so we return 2.

```

**Example 2:**

```

**Input:** x = 8
**Output:** 2
**Explanation:** The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

```

**Constraints:**

- `0 <= x <= 2^31 - 1`

## Video Explanation

[Sqrt(x) - Leetcode 69 - Python](https://www.youtube.com/watch?v=zdMhGxRWutQ)

## Approach

### Intuition

The integer square root is the greatest integer whose square does not exceed x.

### Brute Force

Increment candidates until the next square would be too large.

### Optimal

Binary-search the last candidate satisfying candidate <= x // candidate.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(sqrt(x)) | O(1) |
| Optimal | O(log x) | O(1) |

### Edge cases

- Zero and one are their own integer square roots.
- A perfect square returns its exact root.
- For non-squares, return the floor of the real square root.
