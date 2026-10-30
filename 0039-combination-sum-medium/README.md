# 39. Combination Sum

**Difficulty:** Medium  
**Tags:** Array, Backtracking  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/combination-sum/](https://leetcode.com/problems/combination-sum/)

## Problem

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of* `candidates`* where the chosen numbers sum to* `target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

**Example 1:**

```

**Input:** candidates = [2,3,6,7], target = 7
**Output:** [[2,2,3],[7]]
**Explanation:**
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

```

**Example 2:**

```

**Input:** candidates = [2,3,5], target = 8
**Output:** [[2,2,2,2],[2,3,3],[3,5]]

```

**Example 3:**

```

**Input:** candidates = [2], target = 1
**Output:** []

```

**Constraints:**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

## Video Explanation

[Combination Sum - Backtracking - Leetcode 39 - Python](https://www.youtube.com/watch?v=GBKI9VSKdGg)

## Approach

### Intuition

Choose candidates in a fixed order and recurse on the remaining target; reuse is allowed by staying at the same index.

### Brute Force

Enumerate candidate multisets and retain those summing to target.

### Optimal

Backtrack with a start index, pruning candidates larger than the remaining target.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(target/minCandidate) |
| Optimal | O(N^(T/M)) | O(T/M) |

### Edge cases

- A candidate equal to the remainder completes a result.
- Sort candidates so a too-large value ends the loop.
