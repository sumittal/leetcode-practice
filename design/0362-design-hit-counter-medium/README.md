# 362. Design Hit Counter

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Design, Queue, Data Stream  
**Companies:** Databricks, Dropbox, Careem, Apple, Reddit, Uber, Wise, Roblox, Coupang, Cloudflare, Affirm, Snowflake, OpenAI, Yandex, Snap (+7 more)  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-hit-counter/](https://leetcode.com/problems/design-hit-counter/)

## Problem

Create a counter for events arriving at integer timestamps. It must support recording an event and reporting how many events occurred during the most recent five minutes, including the query timestamp. Example 1: record events at times 1, 2, and 3; asking at time 4 returns 3. Example 2: record at 1, 300, and 301; asking at 301 returns 2 because time 1 has left the 300-second window. Constraints: timestamps are nondecreasing, and the structure receives many hit and count requests.

## Video Explanation

[YouTube search: Search YouTube for leetcode 362 Design Hit Counter neetcode](https://www.youtube.com/results?search_query=leetcode+362+Design+Hit+Counter+neetcode)

## Approach

### Intuition

Only timestamps in the current 300-second window can affect a query.

### Brute Force

Store every hit and scan all timestamps to count those still in range.

### Optimal

Aggregate consecutive hits with the same timestamp in a deque and discard expired timestamp groups from the front.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | hit O(1), getHits O(n) | O(n) |
| Optimal | hit O(1), getHits O(1) amortized | O(300) |

### Edge cases

- Several hits may share one timestamp.
- A hit exactly 300 seconds before the query is expired.
