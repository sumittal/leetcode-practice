# 281. Zigzag Iterator

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Design, Queue, Iterator  
**Companies:** Coinbase, Google, Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/zigzag-iterator/](https://leetcode.com/problems/zigzag-iterator/)

## Problem

Iterate over two lists by alternating available values while preserving each list's order. Example 1: [1, 2] and [3, 4, 5, 6] produce 1, 3, 2, 4, 5, 6. Example 2: [1] and an empty list produce only 1. Constraints: each input list contains integers and the total number of calls is finite.

## Video Explanation

[YouTube search: Search YouTube for leetcode 281 Zigzag Iterator neetcode](https://www.youtube.com/results?search_query=leetcode+281+Zigzag+Iterator+neetcode)

## Approach

### Intuition

A queue of active iterators naturally cycles across lists and drops exhausted ones.

### Brute Force

Materialize the complete alternating output before returning any value.

### Optimal

Queue iterators with remaining elements; pop one, consume a value, then append it again if it is still active.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n + m), next O(1), hasNext O(1) | O(n + m) |
| Optimal | next O(1), hasNext O(1) | O(k) iterators |

### Edge cases

- Either input list may be empty.
- Once one iterator is exhausted, the other continues alone.
