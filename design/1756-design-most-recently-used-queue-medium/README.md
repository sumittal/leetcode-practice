# 1756. Design Most Recently Used Queue

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Linked List, Divide and Conquer, Design, Simulation, Doubly-Linked List, Sqrt Decomposition, Treap, Splay Tree  
**Companies:** Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-most-recently-used-queue/](https://leetcode.com/problems/design-most-recently-used-queue/)

## Problem

Build a queue containing the values 1 through n in order. A fetch request selects the current kth value, returns it, and moves it to the back of the queue. Example 1: for n = 8, fetch(3), fetch(5), fetch(2), fetch(8) returns 3, 6, 2, 2. Example 2: for n = 1, fetch(1) always returns 1. Constraints: n and k are positive, and at most 2000 fetch operations are performed.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1756 Design Most Recently Used Queue neetcode](https://www.youtube.com/results?search_query=leetcode+1756+Design+Most+Recently+Used+Queue+neetcode)

## Approach

### Intuition

Fetching changes the order, so the structure must support both selecting by current rank and appending at the tail.

### Brute Force

Store values in a list, remove the kth value, and append it.

### Optimal

Use a Fenwick tree over active positions. Remove the selected rank and insert the value at a fresh tail position.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | fetch O(n) | O(n) |
| Optimal | fetch O(log(n + q)) | O(n + q), where q is the number of fetches |

### Edge cases

- Fetching the first or last current item moves that same item to the back.
- The append index must keep increasing so old Fenwick positions are never reused.
