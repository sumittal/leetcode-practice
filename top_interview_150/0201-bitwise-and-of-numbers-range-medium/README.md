# 201. Bitwise AND of Numbers Range

**Difficulty:** Medium  
**Tags:** Bit Manipulation  
**Companies:** Microsoft, Google, Amazon, Bloomberg, Meta  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/bitwise-and-of-numbers-range/](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

## Problem

Given two integers `left` and `right` that represent the range `[left, right]`, return *the bitwise AND of all numbers in this range, inclusive*.

**Example 1:**

```

**Input:** left = 5, right = 7
**Output:** 4

```

**Example 2:**

```

**Input:** left = 0, right = 0
**Output:** 0

```

**Example 3:**

```

**Input:** left = 1, right = 2147483647
**Output:** 0

```

**Constraints:**

- `0 <= left <= right <= 2^31 - 1`

## Video Explanation

[YouTube search: Search YouTube for leetcode 201 Bitwise AND of Numbers Range neetcode](https://www.youtube.com/results?search_query=leetcode+201+Bitwise+AND+of+Numbers+Range+neetcode)

## Approach

### Intuition

Any bit that changes while counting through the interval cannot remain set in the range-wide AND.

### Brute Force

AND every integer from left through right.

### Optimal

Right-shift both endpoints until their common binary prefix remains, then shift it back.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(right - left) | O(1) |
| Optimal | O(log right) | O(1) |

### Edge cases

- Equal endpoints return that endpoint.
- An interval crossing a power-of-two boundary clears lower common bits.
- A range including zero returns zero.
