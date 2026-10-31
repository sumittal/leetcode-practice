# 1429. First Unique Number

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Design, Queue, Data Stream  
**Companies:** Uber, Amazon, Microsoft, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/first-unique-number/](https://leetcode.com/problems/first-unique-number/)

## Problem

Maintain a stream of numbers and report its earliest value that has appeared exactly once. Example 1: initialize with [2, 3, 5]; the first unique is 2, then after adding 2 it becomes 3. Example 2: after adding 3 and then 5, the remaining first unique values progress to 5 and then -1. Constraints: stream values are positive integers and operations are interleaved.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1429 First Unique Number neetcode](https://www.youtube.com/results?search_query=leetcode+1429+First+Unique+Number+neetcode)

## Approach

### Intuition

Counts identify duplicates, while a queue preserves arrival order among possible unique values.

### Brute Force

After every insertion, recount the entire stream in order.

### Optimal

Track frequencies and lazily discard non-unique values from the front of an arrival deque.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add O(n), showFirstUnique O(n) | O(n) |
| Optimal | add O(1), showFirstUnique O(1) amortized | O(n) |

### Edge cases

- The stream may contain no unique value, in which case return -1.
- A value that becomes duplicated stays out of the unique queue.
