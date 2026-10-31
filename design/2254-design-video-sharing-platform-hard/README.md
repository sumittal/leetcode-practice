# 2254. Design Video Sharing Platform

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Hash Table, Design, Heap (Priority Queue)  
**Companies:** Google  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-video-sharing-platform/](https://leetcode.com/problems/design-video-sharing-platform/)

## Problem

Create a platform that assigns the smallest available nonnegative ID to each uploaded digit-string video. Support removing a video, watching an inclusive minute range, recording likes and dislikes, and retrieving engagement counts. Example 1: upload "123" receives ID 0; watching minutes 0 through 5 returns "123" and increments views. Example 2: after removing ID 0, the next upload reuses ID 0. Constraints: videos are digit strings, and video IDs are reused after removal.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2254 Design Video Sharing Platform neetcode](https://www.youtube.com/results?search_query=leetcode+2254+Design+Video+Sharing+Platform+neetcode)

## Approach

### Intuition

Video metadata is keyed by ID, while a min-heap tracks freed IDs so uploads reuse the smallest one.

### Brute Force

Scan all IDs to find the smallest free one and scan all video records for each query.

### Optimal

Use a dictionary for active videos and counters, plus a min-heap of reusable IDs and a monotonic next ID.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | upload O(n), other operations O(1) | O(n) |
| Optimal | upload O(log n), remove/watch/like/dislike/get O(1) | O(n) |

### Edge cases

- Operations on a missing video leave state unchanged and return the specified sentinel.
- The watched end minute is clamped to the last available character.
