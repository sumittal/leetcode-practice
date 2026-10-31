# 346. Moving Average from Data Stream

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Easy  
**Tags:** Array, Design, Queue, Data Stream  
**Companies:** Spotify, Meta, Arista Networks, Qualcomm, Citadel, Google, Amazon, Bloomberg, Microsoft  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/moving-average-from-data-stream/](https://leetcode.com/problems/moving-average-from-data-stream/)

## Problem

Create a running average over the most recent window of at most size readings. Example 1: with window size 3, readings 1, 10, 3, and 5 produce averages 1, 5.5, 14/3, and 6. Example 2: with window size 1, readings 4 and 8 produce 4 and 8. Constraints: the window size is positive and readings arrive one at a time.

## Video Explanation

[YouTube search: Search YouTube for leetcode 346 Moving Average from Data Stream neetcode](https://www.youtube.com/results?search_query=leetcode+346+Moving+Average+from+Data+Stream+neetcode)

## Approach

### Intuition

Maintain the current window's sum so each new average does not require rescanning its values.

### Brute Force

Keep all readings and sum the latest window on each request.

### Optimal

Keep a queue of at most size readings and a running sum, removing the oldest reading when the window fills.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | next O(size) | O(n) |
| Optimal | next O(1) | O(size) |

### Edge cases

- Before the window fills, average all readings received so far.
- A size-one window always returns the latest reading.
