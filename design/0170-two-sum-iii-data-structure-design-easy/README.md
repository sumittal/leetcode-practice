# 170. Two Sum III - Data structure design

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Two Pointers, Design, Data Stream  
**Companies:** LinkedIn  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/two-sum-iii-data-structure-design/](https://leetcode.com/problems/two-sum-iii-data-structure-design/)

## Problem

Build a number collection that supports inserting values and asking whether any pair sums to a target. Example 1: add 1 and 3, then find 4 returns true. Example 2: add 3 twice, then find 6 returns true while find 3 is false. Constraints: duplicate values are permitted and a pair must use two distinct inserted elements.

## Video Explanation

[YouTube search: Search YouTube for leetcode 170 Two Sum III - Data structure design neetcode](https://www.youtube.com/results?search_query=leetcode+170+Two+Sum+III+-+Data+structure+design+neetcode)

## Approach

### Intuition

A frequency map lets a target check distinguish two equal values from one occurrence.

### Brute Force

Store all values and inspect every pair for each requested sum.

### Optimal

Store frequencies and scan distinct values, checking the complement and multiplicity when both values are equal.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add O(1), find O(n^2) | O(n) |
| Optimal | add O(1), find O(u) | O(u) |

### Edge cases

- A value cannot pair with itself unless it was added at least twice.
- Values may be negative or repeated.
