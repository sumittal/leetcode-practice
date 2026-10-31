# 77. Combinations

**Difficulty:** Medium  
**Tags:** Backtracking  
**Companies:** Meta, Infosys, IBM, Bloomberg, Amazon, Google, Microsoft  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/combinations/](https://leetcode.com/problems/combinations/)

## Problem

Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

**Example 1:**

```

**Input:** n = 4, k = 2
**Output:** [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
**Explanation:** There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

```

**Example 2:**

```

**Input:** n = 1, k = 1
**Output:** [[1]]
**Explanation:** There is 1 choose 1 = 1 total combination.

```

**Constraints:**

- `1 <= n <= 20`
- `1 <= k <= n`

## Video Explanation

[Combinations - Leetcode 77 - Python](https://www.youtube.com/watch?v=q0s6m7AiM7o)

## Approach

### Intuition

Every combination is an increasing sequence of k choices from 1 through n, so choosing each next value avoids duplicate permutations.

### Brute Force

Generate all subsets of the range and retain those with exactly k elements.

### Optimal

Backtrack over increasing candidates and stop each branch once k values have been chosen.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(k) excluding output |
| Optimal | O(k * C(n,k)) | O(k) excluding output |

### Edge cases

- When k equals n, there is one combination containing every value.
- The increasing candidate order prevents duplicate arrangements.
- Backtrack by removing each appended choice before trying the next.
