# 288. Unique Word Abbreviation

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, String, Design  
**Companies:** The Trade Desk, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/unique-word-abbreviation/](https://leetcode.com/problems/unique-word-abbreviation/)

## Problem

Determine whether a word's abbreviation identifies only that word in a dictionary. An abbreviation keeps the first and last letters and replaces the middle with its length. Example 1: in [deer, door, cake, card], cart is unique because its abbreviation is not used by any dictionary word. Example 2: dear is not unique because it shares an abbreviation with deer and door. Constraints: words contain lowercase letters, and duplicate dictionary entries do not create a different word.

## Video Explanation

[YouTube search: Search YouTube for leetcode 288 Unique Word Abbreviation neetcode](https://www.youtube.com/results?search_query=leetcode+288+Unique+Word+Abbreviation+neetcode)

## Approach

### Intuition

Uniqueness depends only on the set of distinct dictionary words sharing one abbreviation.

### Brute Force

For each query, abbreviate every dictionary entry and compare it with the query abbreviation.

### Optimal

Precompute abbreviation-to-word sets and check whether the set is empty or contains only the queried word.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), isUnique O(n * L) | O(n) |
| Optimal | construction O(total characters), isUnique O(L) | O(n) |

### Edge cases

- Words of length one or two abbreviate to themselves.
- Repeated copies of the queried word still count as one distinct word.
