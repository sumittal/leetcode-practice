# 933. Number of Recent Calls

**Difficulty:** Easy  
**Tags:** Design, Queue, Data Stream  
**Companies:** Databricks, Roblox, Bloomberg, Yandex, Meta, Amazon, Google, Microsoft  
**Pattern:** Design  
**LeetCode:** [https://leetcode.com/problems/number-of-recent-calls/](https://leetcode.com/problems/number-of-recent-calls/)

## Problem

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range `[t - 3000, t]`, that is, the new request plus every earlier request that is no more than `3000` milliseconds older.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

**Example 1:**

```

**Input**
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
**Output**
[null, 1, 2, 3, 3]

**Explanation**
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

```

**Constraints:**

- `1 <= t <= 10^9`
- Each test case will call `ping` with **strictly increasing** values of `t`.
- At most `10^4` calls will be made to `ping`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 933 Number of Recent Calls neetcode](https://www.youtube.com/results?search_query=leetcode+933+Number+of+Recent+Calls+neetcode)

## Approach

### Intuition

Because ping times increase, expired requests leave from the front of a queue.

### Brute Force

Store every request and scan all timestamps for each call.

### Optimal

Append each timestamp and remove requests older than the inclusive 3000-millisecond window.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | ping O(n) | O(n) |
| Optimal | ping O(1) amortized | O(3000) |

### Edge cases

- A request exactly 3000 time units old remains in the window.
- Multiple requests at the same timestamp each count separately.
