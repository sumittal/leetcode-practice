# 40. Combination Sum II

**Difficulty:** Medium  
**Tags:** Array, Backtracking  
**Companies:** Rakuten, Snap, Morgan Stanley, Adobe, Walmart Labs, Zoho, Meta, Microsoft, Bloomberg, LinkedIn, Oracle, TikTok, Google, Amazon, Salesforce  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/combination-sum-ii/](https://leetcode.com/problems/combination-sum-ii/)

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example 1:**

```

**Input:** candidates = [10,1,2,7,6,1,5], target = 8
**Output:**
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

```

**Example 2:**

```

**Input:** candidates = [2,5,2,1,2], target = 5
**Output:**
[
[1,2,2],
[5]
]

```

**Constraints:**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Video Explanation

[Combination Sum II - Backtracking - Leetcode 40 - Python](https://www.youtube.com/watch?v=rSA3t6BDDwg)

## Approach

### Intuition

Sorted candidates allow duplicate choices to be skipped and sums that exceed the target to stop early.

### Brute Force

Enumerate every subset and retain combinations whose values sum to the target.

### Optimal

Backtrack using each candidate at most once, skipping equal values at the same depth and pruning oversized sums.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n 2^n) | O(n) besides output |
| Optimal | O(2^n) in the worst case | O(n) besides output |

### Edge cases

- No subset may reach the target.
- Repeated candidate values can be used only as many times as they occur.
