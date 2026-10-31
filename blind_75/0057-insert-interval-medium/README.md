# 57. Insert Interval

**Difficulty:** Medium  
**Tags:** Array  
**Companies:** Tesco, PhonePe, LinkedIn, Google, Walmart Labs, PayPal, Uber, Microsoft, Apple, Amazon, Meta, Bloomberg, tcs, Oracle, TikTok  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/insert-interval/](https://leetcode.com/problems/insert-interval/)

## Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]` represent the start and the end of the `i^th` interval and `intervals` is sorted in ascending order by `start<sub>i</sub>`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Two intervals are considered overlapping if they share **at least** one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start<sub>i</sub>` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals`* after the insertion*.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

**Example 1:**

```

**Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Output:** [[1,5],[6,9]]

```

**Example 2:**

```

**Input:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Output:** [[1,2],[3,10],[12,16]]
**Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```

**Constraints:**

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10^5`
- `intervals` is sorted by `start<sub>i</sub>` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Video Explanation

[Insert Interval - Leetcode 57 - Python](https://www.youtube.com/watch?v=A8NUOmlwOlM)

## Approach

### Intuition

Sorted intervals before the new range stay unchanged; overlapping ranges can be folded into its bounds.

### Brute Force

Append and sort all intervals, then merge overlaps.

### Optimal

Append intervals before, merge every overlap, then append the remaining suffix.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- The new interval may overlap none or all existing intervals.
- Touching endpoints count as overlap.
