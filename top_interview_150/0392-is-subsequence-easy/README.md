# 392. Is Subsequence

**Difficulty:** Easy  
**Tags:** Two Pointers, String, Dynamic Programming  
**Companies:** Wix, Tinkoff, Pinterest, Yandex, Virtu Financial, Adobe, Meta, Zoho, Amazon, Google, Microsoft, Infosys, Bloomberg  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/is-subsequence/](https://leetcode.com/problems/is-subsequence/)

## Problem

Given two strings `s` and `t`, return `true`* if* `s`* is a **subsequence** of* `t`*, or* `false`* otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**

```
**Input:** s = "abc", t = "ahbgdc"
**Output:** true

```

**Example 2:**

```
**Input:** s = "axc", t = "ahbgdc"
**Output:** false

```

**Constraints:**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say `s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## Video Explanation

[Is Subsequence - Leetcode 392](https://www.youtube.com/watch?v=99RVfqklbCE)

## Approach

### Intuition

A subsequence is formed by matching the requested characters in order while allowing gaps in the source.

### Brute Force

Enumerate subsequences of t and compare each one with s.

### Optimal

Advance a pointer in s whenever the next source character matches it during one scan of t.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- An empty s is a subsequence of every t.
- A longer s cannot match a shorter t.
- Repeated characters must be matched in order.
