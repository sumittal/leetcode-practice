# 567. Permutation in String

**Difficulty:** Medium  
**Tags:** Hash Table, Two Pointers, String, Sliding Window  
**Companies:** Yandex, VK, Walmart Labs, Databricks, Microsoft, Media.net, Amazon, Adobe, Bloomberg, tcs, Meta, Google, Cisco, Salesforce, Oracle (+1 more)  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/permutation-in-string/](https://leetcode.com/problems/permutation-in-string/)

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```

**Example 2:**

```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```

**Constraints:**

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Video Explanation

[Permutation in String - Leetcode 567 - Python](https://www.youtube.com/watch?v=UbyhOgBN834)

## Approach

### Intuition

A fixed-size window is a permutation exactly when its character counts match the pattern's counts.

### Brute Force

Sort each window of the pattern's length and compare it with the sorted pattern.

### Optimal

Maintain character frequencies for a window of fixed length and compare with the pattern frequencies.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((n-m+1) m log m) | O(m) |
| Optimal | O(n + alphabet) | O(alphabet) |

### Edge cases

- A pattern longer than the text cannot be contained.
- Repeated characters require matching multiplicities.
