# 46. Permutations

**Difficulty:** Medium  
**Tags:** Array, Backtracking  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)

## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

**Example 2:**

```
**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

```

**Example 3:**

```
**Input:** nums = [1]
**Output:** [[1]]

```

**Constraints:**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Video Explanation

[Backtracking: Permutations - Leetcode 46 - Python](https://www.youtube.com/watch?v=s7AvT7cGdSo)

## Approach

### Intuition

A permutation is formed by choosing one unused input value at each position.

### Brute Force

Generate every ordering and store the results.

### Optimal

Backtrack with a used marker per index, adding and undoing one choice at each depth.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n * n!) | O(n * n!) for output |
| Optimal | O(n * n!) | O(n) besides output |

### Edge cases

- An empty input has one empty permutation.
- Distinct input values ensure each ordering is unique.
