# 242. Valid Anagram

**Difficulty:** Easy  
**Tags:** Hash Table, String, Sorting  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Video Explanation

[Valid Anagram - Leetcode 242 - Python](https://www.youtube.com/watch?v=9UtInBqnCgA)

## Approach

### Intuition

Two strings are anagrams exactly when every character appears the same number of times in both strings.

### Brute Force

Sort both strings and compare the resulting character sequences.

### Optimal

Count the characters in one string and subtract the counts from the other; all counts must finish at zero.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(n) | O(k) |

### Edge cases

- Different lengths cannot be anagrams.
- Empty strings are anagrams.
- Character counts must include repeated characters.
