# 2276. Count Integers in Intervals

**Difficulty:** Hard  
**Tags:** Design, Segment Tree, Ordered Set  
**Companies:** LinkedIn, Databricks, Uber, Google  
**Pattern:** Design  
**LeetCode:** [https://leetcode.com/problems/count-integers-in-intervals/](https://leetcode.com/problems/count-integers-in-intervals/)

## Problem

Given an **empty** set of intervals, implement a data structure that can:

- **Add** an interval to the set of intervals.
- **Count** the number of integers that are present in **at least one** interval.

Implement the `CountIntervals` class:

- `CountIntervals()` Initializes the object with an empty set of intervals.
- `void add(int left, int right)` Adds the interval `[left, right]` to the set of intervals.
- `int count()` Returns the number of integers that are present in **at least one** interval.

**Note** that an interval `[left, right]` denotes all the integers `x` where `left <= x <= right`.

**Example 1:**

```

**Input**
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
**Output**
[null, null, null, 6, null, 8]

**Explanation**
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals.
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].

```

**Constraints:**

- `1 <= left <= right <= 10^9`
- At most `10^5` calls **in total** will be made to `add` and `count`.
- At least **one** call will be made to `count`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2276 Count Integers in Intervals neetcode](https://www.youtube.com/results?search_query=leetcode+2276+Count+Integers+in+Intervals+neetcode)

## Approach

### Intuition

The structure only needs the number of covered points, not the history of every interval insertion.

### Brute Force

Store all inserted intervals and merge or enumerate them whenever a count is requested.

### Optimal

Use a dynamic segment tree over the bounded integer domain; each node stores covered length and skips fully covered segments.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add O(n log n), count O(n log n) | O(n) |
| Optimal | add O(log U) for the fixed coordinate domain in typical tree updates, count O(1) | O(q log U) |

### Edge cases

- Adding a fully covered range does not change the total.
- Inclusive interval endpoints contribute right - left + 1 points.
