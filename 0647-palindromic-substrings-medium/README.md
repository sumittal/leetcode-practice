# 647. Palindromic Substrings

**Difficulty:** Medium  
**Tags:** Two Pointers, String, Dynamic Programming  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/palindromic-substrings/](https://leetcode.com/problems/palindromic-substrings/)

## Problem

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```

**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".

```

**Example 2:**

```

**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Video Explanation

[Palindromic Substrings - Leetcode 647 - Python](https://www.youtube.com/watch?v=4RACzI5-du8)

## Approach

### Intuition

Each palindromic substring has a center that can be expanded while its endpoints match.

### Brute Force

Test all O(n^2) substrings character by character.

### Optimal

Expand around every odd and even center and count each successful expansion.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^3) | O(1) |
| Optimal | O(n^2) | O(1) |

### Edge cases

- Count each center expansion separately, even for equal substrings.
- Two-character palindromes use an even center.
