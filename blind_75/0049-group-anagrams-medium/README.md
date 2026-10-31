# 49. Group Anagrams

**Difficulty:** Medium  
**Tags:** Array, Hash Table, String, Sorting  
**Companies:** Avito, blinkit, Smartsheet, Adobe, Yelp, Workday, Zoho, HashedIn, Okta, Nike, Wissen Technology, Disney, DP world, Sigmoid, Squarepoint Capital (+60 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**Constraints:**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Video Explanation

[Group Anagrams - Categorize Strings by Count - Leetcode 49](https://www.youtube.com/watch?v=vzdNOK2oB2E)

## Approach

### Intuition

Anagrams have the same character counts, so a canonical representation of those counts can group words together.

### Brute Force

For each word, compare its sorted characters against the representative of each existing group.

### Optimal

Use the tuple of 26 lowercase-letter counts as a dictionary key and append each word to that key's group.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2 k log k) | O(nk) |
| Optimal | O(nk) | O(nk) |

### Edge cases

- An empty string forms a valid one-word group.
- Repeated letters must be represented by their counts, not just their presence.
- The order of groups and words within groups is not significant.
