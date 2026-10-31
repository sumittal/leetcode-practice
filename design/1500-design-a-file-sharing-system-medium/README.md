# 1500. Design a File Sharing System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, Design, Sorting, Heap (Priority Queue), Data Stream  
**Companies:** Twitch, Google  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-a-file-sharing-system/](https://leetcode.com/problems/design-a-file-sharing-system/)

## Problem

Track users who own numbered chunks on a shared server. Example 1: users join owning [1, 2] and [2, 3]; a request for chunk 2 returns both owners in ascending user-ID order. Example 2: after the first user leaves, its chunks have no owners until another user uploads or requests them. Constraints: chunk IDs lie in the server's fixed range, users receive reusable positive IDs, and request results are sorted.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1500 Design a File Sharing System neetcode](https://www.youtube.com/results?search_query=leetcode+1500+Design+a+File+Sharing+System+neetcode)

## Approach

### Intuition

Both directions of the ownership relation are needed: a user must release all its chunks, and a chunk request must list all owners.

### Brute Force

Store each user's chunks and scan all users whenever a chunk owner list is requested.

### Optimal

Maintain user-to-chunk and chunk-to-user sets, plus a min-heap of reusable user IDs.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | join O(chunks), leave O(chunks + users), request O(users) | O(total ownership pairs) |
| Optimal | join O(chunks + log users), leave O(chunks + log users), request O(owners log owners) | O(total ownership pairs + users) |

### Edge cases

- A user requesting an already-owned chunk does not duplicate ownership.
- A request returns current owners before adding the requester.
