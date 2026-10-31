# 359. Logger Rate Limiter

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Easy  
**Tags:** Hash Table, Design, Data Stream  
**Companies:** Verily, AppFolio, Waymo, Netflix, Palo Alto Networks, Grammarly, Docusign, Deliveroo, Reddit, Patreon, Cloudflare, Roblox, Autodesk, Atlassian, Tesla (+6 more)  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/logger-rate-limiter/](https://leetcode.com/problems/logger-rate-limiter/)

## Problem

Build a message filter that accepts a message only when it has not been accepted during the preceding ten seconds. Example 1: a message at time 1 is accepted and the same message at time 2 is rejected. Example 2: after accepting a message at time 1, another copy at time 11 is accepted. Constraints: calls arrive in nondecreasing timestamp order; timestamps and message text fit ordinary integer and string storage.

## Video Explanation

[YouTube search: Search YouTube for leetcode 359 Logger Rate Limiter neetcode](https://www.youtube.com/results?search_query=leetcode+359+Logger+Rate+Limiter+neetcode)

## Approach

### Intuition

For each message, only the timestamp of its last accepted occurrence matters.

### Brute Force

Keep all accepted message-time pairs and scan recent history for the requested message.

### Optimal

Map each message to its last accepted timestamp and update that entry only when the ten-second interval has elapsed.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | shouldPrintMessage O(n) | O(n) |
| Optimal | shouldPrintMessage O(1) average | O(unique messages) |

### Edge cases

- A repeated message at a time difference of nine seconds is rejected.
- A message becomes eligible again at a difference of exactly ten seconds.
