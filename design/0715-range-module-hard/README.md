# 715. Range Module

**Difficulty:** Hard  
**Tags:** Design, Segment Tree, Ordered Set  
**Companies:** Machine Zone, Coupang, Rubrik, Google, Amazon, Meta  
**Pattern:** Design  
**LeetCode:** [https://leetcode.com/problems/range-module/](https://leetcode.com/problems/range-module/)

## Problem

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as **half-open intervals** and query about them.

A **half-open interval** `[left, right)` denotes all the real numbers `x` where `left <= x < right`.

Implement the `RangeModule` class:

- `RangeModule()` Initializes the object of the data structure.
- `void addRange(int left, int right)` Adds the **half-open interval** `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.
- `boolean queryRange(int left, int right)` Returns `true` if every real number in the interval `[left, right)` is currently being tracked, and `false` otherwise.
- `void removeRange(int left, int right)` Stops tracking every real number currently being tracked in the **half-open interval** `[left, right)`.

**Example 1:**

```

**Input**
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
**Output**
[null, null, null, true, false, true]

**Explanation**
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

```

**Constraints:**

- `1 <= left < right <= 10^9`
- At most `10^4` calls will be made to `addRange`, `queryRange`, and `removeRange`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 715 Range Module neetcode](https://www.youtube.com/results?search_query=leetcode+715+Range+Module+neetcode)

## Approach

### Intuition

Keep tracked half-open intervals disjoint and sorted so updates can merge, split, or preserve only affected segments.

### Brute Force

Represent every integer point in a large bitmap and inspect each point in every operation.

### Optimal

Maintain sorted disjoint intervals; merge overlaps on addition, check coverage on query, and split overlaps on removal.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | addRange O(U), queryRange O(U), removeRange O(U) | O(U) |
| Optimal | addRange O(n), queryRange O(n), removeRange O(n) | O(n) |

### Edge cases

- All ranges are half-open, so the right endpoint is excluded.
- Removing a middle section can leave two tracked pieces.
