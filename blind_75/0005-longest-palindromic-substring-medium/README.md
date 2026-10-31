# 5. Longest Palindromic Substring

**Difficulty:** Medium  
**Tags:** Two Pointers, String, Dynamic Programming, Manacher  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

**Example 1:**

```

**Input:** s = "babad"
**Output:** "bab"
**Explanation:** "aba" is also a valid answer.

```

**Example 2:**

```

**Input:** s = "cbbd"
**Output:** "bb"

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Video Explanation

[Longest Palindromic Substring - Python - Leetcode 5](https://www.youtube.com/watch?v=XYQecbcd6_c)

## Approach

### Intuition

Every palindrome expands symmetrically around a one-character or two-character center.

### Brute Force

Check every substring for palindromicity.

### Optimal

Expand around each odd and even center, retaining the longest range.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^3) | O(1) |
| Optimal | O(n^2) | O(1) |

### Edge cases

- Even-length palindromes need a gap center.
- Either maximum palindrome is acceptable when lengths tie.
