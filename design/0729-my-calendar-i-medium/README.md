# 729. My Calendar I

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Design, Segment Tree, Ordered Set  
**Companies:** Uber, Flexport, Google, Oracle, Apple, Amazon, Microsoft, Meta  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/my-calendar-i/](https://leetcode.com/problems/my-calendar-i/)

## Problem

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

Implement the `MyCalendar` class:

- `MyCalendar()` Initializes the calendar object.
- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a **double booking**. Otherwise, return `false` and do not add the event to the calendar.

**Example 1:**

```

**Input**
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
**Output**
[null, true, false, true]

**Explanation**
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

**Constraints:**

- `0 <= start < end <= 10^9`
- At most `1000` calls will be made to `book`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 729 My Calendar I neetcode](https://www.youtube.com/results?search_query=leetcode+729+My+Calendar+I+neetcode)

## Approach

### Intuition

Two half-open bookings conflict exactly when their intervals overlap with positive length.

### Brute Force

Check every existing booking for overlap before appending a new one.

### Optimal

Keep bookings sorted by start and inspect only the predecessor and successor around the insertion point.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | book O(n) | O(n) |
| Optimal | book O(log n) search plus O(n) insertion | O(n) |

### Edge cases

- An event ending exactly when another begins is allowed.
- A rejected booking must not change the stored intervals.
