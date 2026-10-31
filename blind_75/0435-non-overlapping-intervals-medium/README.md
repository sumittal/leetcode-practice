# 435. Non-overlapping Intervals

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Greedy, Sorting  
**Companies:** Grammarly, Verkada, Zoho, IBM, Amazon, PayPal, Bloomberg, Visa, Roblox, tcs, TikTok, Google, Meta, Microsoft, Oracle (+2 more)  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/non-overlapping-intervals/](https://leetcode.com/problems/non-overlapping-intervals/)

## Problem

Given an array of intervals `intervals` where `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

**Note** that intervals which only touch at a point are **non-overlapping**. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

**Example 1:**

```

**Input:** intervals = [[1,2],[2,3],[3,4],[1,3]]
**Output:** 1
**Explanation:** [1,3] can be removed and the rest of the intervals are non-overlapping.

```

**Example 2:**

```

**Input:** intervals = [[1,2],[1,2],[1,2]]
**Output:** 2
**Explanation:** You need to remove two [1,2] to make the rest of the intervals non-overlapping.

```

**Example 3:**

```

**Input:** intervals = [[1,2],[2,3]]
**Output:** 0
**Explanation:** You don't need to remove any of the intervals since they're already non-overlapping.

```

**Constraints:**

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start<sub>i</sub> < end<sub>i</sub> <= 5 * 10^4`

## Video Explanation

[Non-Overlapping Intervals - Leetcode 435 - Python](https://www.youtube.com/watch?v=nONCGxWoUfM)

## Approach

### Intuition

Keeping the interval that ends first leaves the most room for later intervals.

### Brute Force

Try every subset of intervals and maximize a non-overlapping subset.

### Optimal

Sort by end time and greedily retain each interval starting at or after the last retained end.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n log n) | O(n) |

### Edge cases

- Equal endpoints are non-overlapping under the problem definition.
- Identical intervals require removing all but one.
