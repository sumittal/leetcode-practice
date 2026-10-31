# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy  
**Tags:** Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm  
**Companies:** Pocket Gems, tcs, Capgemini, Zoho, Microsoft, Qualcomm, Cognizant, Bloomberg, Google, Amazon, Expedia, Apple, Meta, PayPal, Infosys (+1 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

```

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

```

**Example 2:**

```

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.

```

**Constraints:**

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Video Explanation

[Knuth–Morris–Pratt KMP - Find the Index of the First Occurrence in a String - Leetcode 28 - Python](https://www.youtube.com/watch?v=JoF0Z7nVSrA)

## Approach

### Intuition

KMP remembers how much of the needle already matches when a text character causes a mismatch.

### Brute Force

Try matching the needle at every possible starting index in the haystack.

### Optimal

Build the needle's longest-prefix-suffix table and use it to skip redundant comparisons during the scan.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nm) | O(1) |
| Optimal | O(n+m) | O(m) |

### Edge cases

- An empty needle matches at index zero.
- A needle longer than the haystack cannot match.
- A partial overlap in the needle must be reused after a mismatch.
