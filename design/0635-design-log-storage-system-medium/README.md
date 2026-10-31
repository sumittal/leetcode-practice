# 635. Design Log Storage System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, String, Design, Ordered Set  
**Companies:** Snap, Snowflake, Apple, Amazon  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-log-storage-system/](https://leetcode.com/problems/design-log-storage-system/)

## Problem

Keep timestamped log identifiers and return those in a requested inclusive time span at one of six granularities. Example 1: after recording two logs in January and one in February, a January-month query returns the first two IDs in time order. Example 2: a query restricted to one second returns only logs whose timestamp has that exact second. Constraints: timestamps use the fixed YYYY:MM:DD:HH:MM:SS layout, IDs are unique, and granularity is Year, Month, Day, Hour, Minute, or Second.

## Video Explanation

[YouTube search: Search YouTube for leetcode 635 Design Log Storage System neetcode](https://www.youtube.com/results?search_query=leetcode+635+Design+Log+Storage+System+neetcode)

## Approach

### Intuition

A fixed timestamp format makes prefix comparison sufficient to truncate the requested granularity.

### Brute Force

Store every log and scan all records on each retrieval.

### Optimal

Keep records ordered by timestamp, compare the relevant timestamp prefixes, and emit matching IDs in order.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | put O(1), retrieve O(n log n) to return chronological IDs | O(n) |
| Optimal | put O(n), retrieve O(n) | O(n) |

### Edge cases

- Both endpoints are inclusive at the selected granularity.
- Several logs may share one timestamp.
