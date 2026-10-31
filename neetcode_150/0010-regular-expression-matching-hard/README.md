# 10. Regular Expression Matching

**Difficulty:** Hard  
**Tags:** String, Dynamic Programming, Recursion  
**Companies:** Netskope, X, Rokt, Zoho, Waymo, Airbnb, ByteDance, Coupang, Two Sigma, Amazon, Sprinklr, Bloomberg, TikTok, PhonePe, Uber (+9 more)  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)

## Problem

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

**Example 1:**

```

**Input:** s = "aa", p = "a"
**Output:** false
**Explanation:** "a" does not match the entire string "aa".

```

**Example 2:**

```

**Input:** s = "aa", p = "a*"
**Output:** true
**Explanation:** '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

```

**Example 3:**

```

**Input:** s = "ab", p = ".*"
**Output:** true
**Explanation:** ".*" means "zero or more (*) of any character (.)".

```

**Constraints:**

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

## Video Explanation

[Regular Expression Matching - Dynamic Programming Top-Down Memoization - Leetcode 10](https://www.youtube.com/watch?v=HAA8mgxlov8)

## Approach

### Intuition

A literal or dot consumes one matching character, while a star can either erase its preceding token or repeat it.

### Brute Force

Recursively branch over each matching token and all valid repetition counts for stars.

### Optimal

Use prefix DP; for star, combine the zero-occurrence state two pattern positions back with a one-more-match state in the same star column.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(m+n) |
| Optimal | O(mn) | O(mn) |

### Edge cases

- An empty string matches only patterns reducible to empty through star pairs.
- A dot matches any one character, but a star modifies only its preceding token.
