# 3369. Design an Array Statistics Tracker 

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Hash Table, Binary Search, Design, Queue, Heap (Priority Queue), Data Stream, Ordered Set  
**Companies:** Amazon  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-an-array-statistics-tracker/](https://leetcode.com/problems/design-an-array-statistics-tracker/)

## Problem

Maintain a multiset that supports appending values, removing the earliest appended value, and querying the floored mean, upper median, and mode. If several values tie for highest frequency, the smallest value is the mode. Example 1: values [1, 2, 2] have mean 1, median 2, and mode 2. Example 2: [1, 2, 2, 1] has tied modes and returns 1; after removing the oldest 1, the mode becomes 2. Constraints: values are positive, there are at most 100000 total operations, and queries/removals occur only when the multiset is nonempty.

## Video Explanation

[YouTube search: Search YouTube for leetcode 3369 Design an Array Statistics Tracker  neetcode](https://www.youtube.com/results?search_query=leetcode+3369+Design+an+Array+Statistics+Tracker++neetcode)

## Approach

### Intuition

A FIFO queue identifies expirations; an order-statistic tree, running sum, and lazy frequency heap maintain the three statistics.

### Brute Force

Keep the active values in a list and recompute a sorted copy and frequency counts for each query.

### Optimal

Combine a deque, running sum, randomized treap with subtree sizes, and a lazy max-heap keyed by frequency then value.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add/remove O(n), mean O(1), median/mode O(n log n) | O(n) |
| Optimal | add/remove O(log n), mean O(1), median O(log n), mode O(log n) amortized | O(n) |

### Edge cases

- The median is the larger of the two middle values when the size is even.
- Frequency ties choose the smallest value, including after FIFO removals.
