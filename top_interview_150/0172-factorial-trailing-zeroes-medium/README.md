# 172. Factorial Trailing Zeroes

**Difficulty:** Medium  
**Tags:** Math  
**Companies:** Bloomberg, tcs, Google, Microsoft, Amazon, Meta  
**Pattern:** Math  
**LeetCode:** [https://leetcode.com/problems/factorial-trailing-zeroes/](https://leetcode.com/problems/factorial-trailing-zeroes/)

## Problem

Given an integer `n`, return *the number of trailing zeroes in* `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

**Example 1:**

```

**Input:** n = 3
**Output:** 0
**Explanation:** 3! = 6, no trailing zero.

```

**Example 2:**

```

**Input:** n = 5
**Output:** 1
**Explanation:** 5! = 120, one trailing zero.

```

**Example 3:**

```

**Input:** n = 0
**Output:** 0

```

**Constraints:**

- `0 <= n <= 10^4`

**Follow up:** Could you write a solution that works in logarithmic time complexity?

## Video Explanation

[YouTube search: Search YouTube for leetcode 172 Factorial Trailing Zeroes neetcode](https://www.youtube.com/results?search_query=leetcode+172+Factorial+Trailing+Zeroes+neetcode)

## Approach

### Intuition

Each trailing zero needs a factor pair 2 times 5, and factorials contain more factors of 2 than 5.

### Brute Force

Factor every integer from one through n and count each factor of five.

### Optimal

Repeatedly divide n by five and sum the quotients to count factors contributed by powers of five.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(1) |
| Optimal | O(log_5 n) | O(1) |

### Edge cases

- Values below five have no trailing zeros.
- Multiples of 25 contribute an additional factor of five.
- Zero factorial has zero trailing zeros.
