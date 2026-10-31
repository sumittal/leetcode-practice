# 3885. Design Event Manager

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Design, Heap (Priority Queue), Ordered Set  
**Companies:** Goldman Sachs  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-event-manager/](https://leetcode.com/problems/design-event-manager/)

## Problem

You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

Implement the `EventManager` class:

- `EventManager(int[][] events)` Initializes the manager with the given events, where `events[i] = [eventId<sub>i</sub>, priority<sub>​​​​​​​i</sub>]`.
- `void updatePriority(int eventId, int newPriority)` Updates the priority of the **active** event with id `eventId` to `newPriority`.
- `int pollHighest()` Removes and returns the `eventId` of the **active** event with the **highest** priority. If multiple active events have the same priority, return the **smallest** `eventId` among them. If there are no active events, return -1.

An event is called **active** if it has not been removed by `pollHighest()`.

**Example 1:**

**Input:**
["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]
[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]

**Output:**
[null, 2, null, 5, 9]

**Explanation**

EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events
eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2
eventManager.updatePriority(9, 7); // event 9 now has priority 7
eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5
eventManager.pollHighest(); // return 9

**Example 2:**

**Input:**
["EventManager", "pollHighest", "pollHighest", "pollHighest"]
[[[[4, 1], [7, 2]]], [], [], []]

**Output:**
[null, 7, 4, -1]

**Explanation**

EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events
eventManager.pollHighest(); // return 7
eventManager.pollHighest(); // return 4
eventManager.pollHighest(); // no events remain, return -1

**Constraints:**

- `1 <= events.length <= 10^5`
- `events[i] = [eventId, priority]`
- `1 <= eventId <= 10^9`
- `1 <= priority <= 10^9`
- All the values of `eventId` in `events` are **unique**.
- `1 <= newPriority <= 10^9`
- For every call to `updatePriority`, `eventId` refers to an **active** event.
- At most `10^5` calls in **total** will be made to `updatePriority` and `pollHighest`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 3885 Design Event Manager neetcode](https://www.youtube.com/results?search_query=leetcode+3885+Design+Event+Manager+neetcode)

## Approach

### Intuition

A max-priority queue exposes the event to poll, while versioned entries make priority changes cheap.

### Brute Force

Store events in a map and scan all active events for every poll.

### Optimal

Map active IDs to current priority and version, and keep a lazy heap ordered by priority descending then ID ascending.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | updatePriority O(1), pollHighest O(n) | O(n) |
| Optimal | updatePriority O(log n), pollHighest O(log n) amortized | O(n + updates) |

### Edge cases

- Equal priorities choose the smallest event ID.
- Heap entries from older priority updates are discarded when they reach the top.
