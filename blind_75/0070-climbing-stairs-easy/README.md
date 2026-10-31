# 70. Climbing Stairs

**Difficulty:** Easy  
**Tags:** Math, Dynamic Programming, Memoization  
**Companies:** HPE, HSBC, Adobe, Rakuten, Grammarly, Zoho, Accenture, AMD, Qualcomm, Bloomberg, Infosys, Amazon, Microsoft, Accolite, Google (+18 more)  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

## Problem

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

**Constraints:**

- `1 <= n <= 45`

## Video Explanation

[Climbing Stairs - Dynamic Programming - Leetcode 70 - Python](https://www.youtube.com/watch?v=Y0lT9Fck7qI)

## Approach

### Intuition

The final step comes from either one step below or two steps below.

### Brute Force

Recursively enumerate one-step and two-step choices.

### Optimal

Keep the previous two Fibonacci counts while moving upward.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- n=1 has one way.
- The recurrence combines the two previous totals.
