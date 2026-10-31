# 56. Merge Intervals

**Difficulty:** Medium  
**Tags:** Array, Sorting, Quicksort  
**Companies:** Tesla, Grammarly, Ripple, Darwinbox, Grubhub, Tesco, X, SAP, Ozon, Nutanix, Zoho, IBM, Yelp, Walmart Labs, Nextdoor (+85 more)  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)

## Problem

Given an array of `intervals` where `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Example 1:**

```

**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]
**Output:** [[1,6],[8,10],[15,18]]
**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

**Example 2:**

```

**Input:** intervals = [[1,4],[4,5]]
**Output:** [[1,5]]
**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.

```

**Example 3:**

```

**Input:** intervals = [[4,7],[1,4]]
**Output:** [[1,7]]
**Explanation:** Intervals [1,4] and [4,7] are considered overlapping.

```

**Constraints:**

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10^4`

## Video Explanation

[Merge Intervals - Sorting - Leetcode 56](https://www.youtube.com/watch?v=44H3cEC2fFM)

## Approach

### Intuition

After sorting by start, any overlap can only involve the most recently merged interval.

### Brute Force

Repeatedly compare and merge every pair until no overlaps remain.

### Optimal

Sort by start and extend the last output interval whenever the next one overlaps.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n log n) | O(n) |

### Edge cases

- Touching endpoints overlap.
- Disjoint intervals are copied as separate output ranges.
