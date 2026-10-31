# 50. Pow(x, n)

**Difficulty:** Medium  
**Tags:** Math, Recursion  
**Companies:** Wix, Meta, eBay, LinkedIn, Bloomberg, tcs, Qualcomm, ServiceNow, Google, Microsoft, Amazon, EPAM Systems, Citadel, Adobe, Walmart Labs (+6 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/powx-n/](https://leetcode.com/problems/powx-n/)

## Problem

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).

**Example 1:**

```

**Input:** x = 2.00000, n = 10
**Output:** 1024.00000

```

**Example 2:**

```

**Input:** x = 2.10000, n = 3
**Output:** 9.26100

```

**Example 3:**

```

**Input:** x = 2.00000, n = -2
**Output:** 0.25000
**Explanation:** 2^-2 = 1/2^2 = 1/4 = 0.25

```

**Constraints:**

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31-1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Video Explanation

[Pow(x, n) - X to the power of N - Leetcode 50 - Python](https://www.youtube.com/watch?v=g9YQyYi4IQQ)

## Approach

### Intuition

Binary exponentiation squares the base and consumes one exponent bit at a time.

### Brute Force

Multiply by x once for each positive exponent step, or divide repeatedly for a negative exponent.

### Optimal

Use exponentiation by squaring and invert the base when the exponent is negative.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(|n|) | O(1) |
| Optimal | O(log |n|) | O(1) |

### Edge cases

- Exponent zero returns one.
- A negative exponent returns the reciprocal of the corresponding positive power.
