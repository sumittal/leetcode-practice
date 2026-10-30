# 338. Counting Bits

**Difficulty:** Easy  
**Tags:** Dynamic Programming, Bit Manipulation  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/counting-bits/](https://leetcode.com/problems/counting-bits/)

## Problem

Given an integer `n`, return *an array* `ans`* of length* `n + 1`* such that for each* `i`** (`0 <= i <= n`)*,* `ans[i]`* is the **number of*** `1`***'s** in the binary representation of* `i`.

Do not solve it with built-in functions (i.e., like `__builtin_popcount` in C++).

**Example 1:**

```

**Input:** n = 2
**Output:** [0,1,1]
**Explanation:**
0 --> 0
1 --> 1
2 --> 10

```

**Example 2:**

```

**Input:** n = 5
**Output:** [0,1,1,2,1,2]
**Explanation:**
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```

**Constraints:**

- `0 <= n <= 10^5`

**Follow up:**

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?

## Video Explanation

[Counting Bits - Dynamic Programming - Leetcode 338 - Python](https://www.youtube.com/watch?v=RyBM56RIWrM)

## Approach

### Intuition

Removing the lowest set bit maps a number to a smaller number whose bit count is already known.

### Brute Force

Count bits independently for every number from 0 through n.

### Optimal

Use dp[x] = dp[x & (x-1)] + 1 for each increasing x.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n*w) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- dp[0] is zero.
- The predecessor is always smaller and already computed.
