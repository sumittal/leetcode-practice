# 78. Subsets

**Difficulty:** Medium  
**Tags:** Array, Backtracking, Bit Manipulation  
**Companies:** Coupang, PornHub, Wix, Bloomberg, Amazon, Meta, Microsoft, Agoda, Uber, Google, PayPal, TikTok, Walmart Labs, Flipkart, tcs (+4 more)  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/subsets/](https://leetcode.com/problems/subsets/)

## Problem

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```

**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

**Example 2:**

```

**Input:** nums = [0]
**Output:** [[],[0]]

```

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Video Explanation

[Subsets - Backtracking - Leetcode 78](https://www.youtube.com/watch?v=REOH22Xwdkk)

## Approach

### Intuition

Each input value creates two choices for a subset: include it or leave it out.

### Brute Force

Enumerate all bitmasks and include each value whose corresponding bit is set.

### Optimal

Backtrack through the input, recording the current subset at each recursion depth.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n 2^n) | O(n 2^n) for output |
| Optimal | O(n 2^n) | O(n) besides output |

### Edge cases

- An empty input produces the single empty subset.
- The input values are distinct, so each subset is unique.
