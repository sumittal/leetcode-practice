# 1143. Longest Common Subsequence

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Longest Common Subsequence  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)

## Problem

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence**.* If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

**Example 1:**

```

**Input:** text1 = "abcde", text2 = "ace"
**Output:** 3
**Explanation:** The longest common subsequence is "ace" and its length is 3.

```

**Example 2:**

```

**Input:** text1 = "abc", text2 = "abc"
**Output:** 3
**Explanation:** The longest common subsequence is "abc" and its length is 3.

```

**Example 3:**

```

**Input:** text1 = "abc", text2 = "def"
**Output:** 0
**Explanation:** There is no such common subsequence, so the result is 0.

```

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Video Explanation

[Longest Common Subsequence - Dynamic Programming - Leetcode 1143](https://www.youtube.com/watch?v=Ua0GhsJSlWM)

## Approach

### Intuition

Matching final characters extend a common subsequence; otherwise one final character can be skipped.

### Brute Force

Recursively branch on skipping either string's last character.

### Optimal

Fill a prefix DP table using the diagonal on matches and the larger neighboring prefix otherwise.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(m+n) |
| Optimal | O(m*n) | O(m*n) |

### Edge cases

- An empty string gives length zero.
- Order is preserved; characters need not be contiguous.
