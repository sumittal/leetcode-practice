# 252. Meeting Rooms

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Easy  
**Tags:** Array, Sorting, Quicksort  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/meeting-rooms/](https://leetcode.com/problems/meeting-rooms/)

## Problem

Given a list of meeting intervals `[start, end]`, determine whether one person can attend every meeting. Two meetings overlap when the later meeting starts before the earlier one ends; meetings that share only a boundary time can both be attended.

**Example 1:**
- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `false`
- Explanation: The meeting from `0` to `30` overlaps both shorter meetings.

**Example 2:**
- Input: `intervals = [[7,10],[2,4]]`
- Output: `true`
- Explanation: The two time ranges do not overlap.

**Constraints:**
- Each interval has `start < end`.
- There are at most `10,000` intervals.

## Video Explanation

[Meeting Rooms - Leetcode 252 - Python](https://www.youtube.com/watch?v=PaJxqZVPhbg)

## Approach

### Intuition

After sorting by start time, any overlap is visible between adjacent meetings.

### Brute Force

Compare every pair of meeting intervals for overlap.

### Optimal

Sort by start and reject when a meeting begins before the previous one ends.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n log n) | O(1) |

### Edge cases

- An empty schedule is attendable.
- A meeting may start exactly when the previous one ends.
