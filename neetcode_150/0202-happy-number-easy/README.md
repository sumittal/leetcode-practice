# 202. Happy Number

**Difficulty:** Easy  
**Tags:** Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm  
**Companies:** Snowflake, BlackRock, Nike, Jump Trading, X, Swiggy, Audible, Airbnb, Autodesk, Google, Microsoft, Accenture, Amazon, Tesla, Cisco (+10 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)

## Problem

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` *if* `n` *is a happy number, and* `false` *if not*.

**Example 1:**

```

**Input:** n = 19
**Output:** true
**Explanation:**
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

```

**Example 2:**

```

**Input:** n = 2
**Output:** false

```

**Constraints:**

- `1 <= n <= 2^31 - 1`

## Video Explanation

[Happy Number - Leetcode 202 - Python](https://www.youtube.com/watch?v=ljz85bxOYJ0)

## Approach

### Intuition

Repeated digit-square sums either reach one or enter a cycle that excludes one.

### Brute Force

Continue computing digit-square sums without recording previously seen values.

### Optimal

Track values already seen and stop when the sequence reaches one or repeats.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Unbounded without cycle detection | O(1) |
| Optimal | O(log n) per distinct sequence value | O(log n) distinct values |

### Edge cases

- One is happy immediately.
- A repeated non-one value proves the sequence is in a cycle.
