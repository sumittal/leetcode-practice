# 1851. Minimum Interval to Include Each Query

**Difficulty:** Hard  
**Tags:** Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)  
**Companies:** Google, Bloomberg, Amazon  
**Pattern:** Intervals  
**LeetCode:** [https://leetcode.com/problems/minimum-interval-to-include-each-query/](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

## Problem

You are given a 2D integer array `intervals`, where `intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]` describes the `i^th` interval starting at `left<sub>i</sub>` and ending at `right<sub>i</sub>` **(inclusive)**. The **size** of an interval is defined as the number of integers it contains, or more formally `right<sub>i</sub> - left<sub>i</sub> + 1`.

You are also given an integer array `queries`. The answer to the `j^th` query is the **size of the smallest interval** `i` such that `left<sub>i</sub> <= queries[j] <= right<sub>i</sub>`. If no such interval exists, the answer is `-1`.

Return *an array containing the answers to the queries*.

**Example 1:**

```

**Input:** intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
**Output:** [3,3,1,4]
**Explanation:** The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

```

**Example 2:**

```

**Input:** intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
**Output:** [2,-1,4,6]
**Explanation:** The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

```

**Constraints:**

- `1 <= intervals.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= left<sub>i</sub> <= right<sub>i</sub> <= 10^7`
- `1 <= queries[j] <= 10^7`

## Video Explanation

[Minimum Interval to Include Each Query - Leetcode 1851 - Python](https://www.youtube.com/watch?v=5hQ5WWW5awQ)

## Approach

### Intuition

When queries are processed in sorted order, every interval that can contain the current query is available to compare by length.

### Brute Force

For every query, scan every interval and select the shortest one containing it.

### Optimal

Sort intervals and indexed queries, maintain eligible intervals in a min-heap by length, and store answers at original query indices.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nq) | O(q) |
| Optimal | O((n+q) log(n+q)) | O(n+q) |

### Edge cases

- A query outside all intervals returns -1.
- Unsorted queries must retain their original answer positions.
