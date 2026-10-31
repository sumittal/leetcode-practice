# 244. Shortest Word Distance II

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Two Pointers, String, Design  
**Companies:** LinkedIn, Anduril, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/shortest-word-distance-ii/](https://leetcode.com/problems/shortest-word-distance-ii/)

## Problem

Build an index over a word sequence so repeated shortest-distance requests can be answered efficiently. Example 1: in [practice, makes, perfect, coding, makes], the distance from coding to practice is 3. Example 2: the distance from coding to makes is 1. Constraints: requested words exist in the input and the two query words differ.

## Video Explanation

[YouTube search: Search YouTube for leetcode 244 Shortest Word Distance II neetcode](https://www.youtube.com/results?search_query=leetcode+244+Shortest+Word+Distance+II+neetcode)

## Approach

### Intuition

For each word, its sorted occurrence positions are enough to locate the closest pair.

### Brute Force

Scan all positions of one word and compare them with every position of the other.

### Optimal

Store sorted position lists and advance two pointers to the nearest matching occurrences.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), shortest O(f1 * f2) | O(n) |
| Optimal | construction O(n), shortest O(f1 + f2) | O(n) |

### Edge cases

- Repeated occurrences may make a later pair closer than the first pair.
- The two queried words are guaranteed to be distinct.
