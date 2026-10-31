# 352. Data Stream as Disjoint Intervals

**Difficulty:** Hard  
**Tags:** Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set  
**Companies:** Bloomberg, Google, Amazon  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/data-stream-as-disjoint-intervals/](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

## Problem

Given a data stream input of non-negative integers `a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:

- `SummaryRanges()` Initializes the object with an empty stream.
- `void addNum(int value)` Adds the integer `value` to the stream.
- `int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[start<sub>i</sub>, end<sub>i</sub>]`. The answer should be sorted by `start<sub>i</sub>`.

**Example 1:**

```

**Input**
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
**Output**
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

**Explanation**
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

```

**Constraints:**

- `0 <= value <= 10^4`
- At most `3 * 10^4` calls will be made to `addNum` and `getIntervals`.
- At most `10^2` calls will be made to `getIntervals`.

**Follow up:** What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?

## Video Explanation

[Data Stream as Disjoint Intervals - Leetcode 352 - Python](https://www.youtube.com/watch?v=FavoZjPIWpo)

## Approach

### Intuition

A new value can only create or join an interval next to its insertion point.

### Brute Force

Store every value and sort and regroup the entire set for each interval request.

### Optimal

Keep sorted, disjoint intervals and merge the predecessor and successor when adjacent.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | addNum O(1), getIntervals O(n log n) | O(n) |
| Optimal | addNum O(n) due to list insertion, getIntervals O(n) | O(n) |

### Edge cases

- Adding an existing value leaves intervals unchanged.
- A value may bridge two adjacent intervals into one.
