# 253. Meeting Rooms II

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/meeting-rooms-ii/](https://leetcode.com/problems/meeting-rooms-ii/)

## Problem

Given meeting intervals `[start, end]`, return the fewest rooms needed to schedule all meetings without overlap. A room becomes available when its current meeting ends, including when another meeting starts at that same time.

**Example 1:**
- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `2`
- Explanation: The meeting from `0` to `30` overlaps each shorter meeting, while the shorter meetings can share one additional room.

**Example 2:**
- Input: `intervals = [[7,10],[2,4]]`
- Output: `1`
- Explanation: The meetings occur at separate times, so one room is sufficient.

**Constraints:**
- Each interval has `start < end`.
- There are at most `10,000` intervals.

## Video Explanation

[Meeting Rooms II - Leetcode 253 - Python](https://www.youtube.com/watch?v=FdzJmTCVyJU)

## Approach

### Intuition

At each start time, rooms are needed only for meetings that have not yet ended.

### Brute Force

For each meeting, count all other intervals overlapping it and track the maximum concurrency.

### Optimal

Sort by start time and use a min-heap of active end times, releasing rooms that have ended.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n log n) | O(n) |

### Edge cases

- An empty schedule needs zero rooms.
- A room is reusable when its meeting ends at the next meeting's start.
