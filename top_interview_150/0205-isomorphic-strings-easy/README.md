# 205. Isomorphic Strings

**Difficulty:** Easy  
**Tags:** Hash Table, String  
**Companies:** Remitly, Sprinklr, Yandex, Zomato, LinkedIn, Bloomberg, Accenture, American Express, Zoho, Amazon, Microsoft, Google, Meta, Oracle, tcs  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/isomorphic-strings/](https://leetcode.com/problems/isomorphic-strings/)

## Problem

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

**Explanation:**

The strings `s` and `t` can be made identical by:

- Mapping `'e'` to `'a'`.
- Mapping `'g'` to `'d'`.

**Example 2:**

**Input:** s = "f11", t = "b23"

**Output:** false

**Explanation:**

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

**Example 3:**

**Input:** s = "paper", t = "title"

**Output:** true

**Constraints:**

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

## Video Explanation

[Isomorphic Strings - Leetcode 205 - Python](https://www.youtube.com/watch?v=7yF-U1hLEqQ)

## Approach

### Intuition

Two strings are isomorphic exactly when each character in either string always maps to one unique character in the other.

### Brute Force

Try every character substitution and compare the transformed string with the target.

### Optimal

Track both source-to-target and target-to-source mappings while scanning aligned characters.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(Σ) |
| Optimal | O(n) | O(Σ) |

### Edge cases

- Strings of different lengths cannot be isomorphic.
- Repeated source characters must map consistently.
- Different source characters cannot share a target character.
