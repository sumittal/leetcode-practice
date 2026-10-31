# 22. Generate Parentheses

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Backtracking, Bracket Sequences  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/generate-parentheses/](https://leetcode.com/problems/generate-parentheses/)

## Problem

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

**Example 1:**

```
**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]

```

**Example 2:**

```
**Input:** n = 1
**Output:** ["()"]

```

**Constraints:**

- `1 <= n <= 8`

## Video Explanation

[Generate Parentheses - Stack - Leetcode 22](https://www.youtube.com/watch?v=s9fokUqJ76A)

## Approach

### Intuition

A valid prefix can add an opening bracket while any remain, and a closing bracket only when it will not unbalance the prefix.

### Brute Force

Generate all strings of length 2n and retain those with balanced prefixes.

### Optimal

Backtrack over only valid prefixes, tracking the number of opened and closed pairs.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^(2n) n) | O(2^(2n)) |
| Optimal | O(Cn) | O(n) besides the output |

### Edge cases

- Zero pairs produce one empty string.
- A closing bracket is never added before its matching opening bracket.
