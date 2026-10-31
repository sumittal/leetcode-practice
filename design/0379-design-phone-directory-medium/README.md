# 379. Design Phone Directory

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Linked List, Design, Queue  
**Companies:** Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-phone-directory/](https://leetcode.com/problems/design-phone-directory/)

## Problem

Manage a fixed range of phone numbers and always assign the smallest unused number. Example 1: with capacity two, successive get calls return 0 and 1, and the next returns -1. Example 2: after releasing 0, the next get returns 0 again. Constraints: allocated numbers are in [0, maxNumbers), and release may be repeated.

## Video Explanation

[YouTube search: Search YouTube for leetcode 379 Design Phone Directory neetcode](https://www.youtube.com/results?search_query=leetcode+379+Design+Phone+Directory+neetcode)

## Approach

### Intuition

A pointer covers numbers never issued, while a min-heap orders explicitly released numbers.

### Brute Force

Scan the whole number range for the smallest free number on each get.

### Optimal

Track the next never-used number, a min-heap of released numbers, and a set preventing duplicate releases.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | get O(n), check/release O(1) | O(n) |
| Optimal | get/release O(log n), check O(1) | O(n) |

### Edge cases

- get returns -1 when every number is assigned.
- Releasing an already free number does not create duplicate availability.
