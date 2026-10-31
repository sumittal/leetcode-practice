# 251. Flatten 2D Vector

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Two Pointers, Design, Iterator  
**Companies:** Zenefits, X, Airbnb, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/flatten-2d-vector/](https://leetcode.com/problems/flatten-2d-vector/)

## Problem

Implement an iterator over a list of integer rows that skips empty rows and yields values in row-major order. Example 1: iterating [[1,2],[3],[4,5,6]] produces 1,2,3,4,5,6. Example 2: iterating [[],[7],[],[8,9]] produces 7,8,9. Constraints: next is called only when another integer exists, and hasNext reports whether one remains.

## Video Explanation

[YouTube search: Search YouTube for leetcode 251 Flatten 2D Vector neetcode](https://www.youtube.com/results?search_query=leetcode+251+Flatten+2D+Vector+neetcode)

## Approach

### Intuition

A stack of row iterators can skip exhausted and empty rows while preserving their original order.

### Brute Force

Flatten every row into a new list when constructing the iterator.

### Optimal

Keep an iterator for the current row and an iterator over remaining rows, advancing past exhausted rows on demand.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | initialization O(n), next O(1), hasNext O(1) | O(n) |
| Optimal | next O(1) amortized, hasNext O(1) amortized | O(number of rows) |

### Edge cases

- Empty rows are skipped without producing values.
- The iterator preserves left-to-right row-major order.
