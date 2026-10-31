# 911. Online Election

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Binary Search, Design  
**Companies:** Google, Bloomberg  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/online-election/](https://leetcode.com/problems/online-election/)

## Problem

You are given two integer arrays `persons` and `times`. In an election, the `i^th` vote was cast for `persons[i]` at time `times[i]`.

For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the `TopVotedCandidate` class:

- `TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.
- `int q(int t)` Returns the number of the person that was leading the election at time `t` according to the mentioned rules.

**Example 1:**

```

**Input**
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
**Output**
[null, 0, 1, 1, 0, 0, 1]

**Explanation**
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1

```

**Constraints:**

- `1 <= persons.length <= 5000`
- `times.length == persons.length`
- `0 <= persons[i] < persons.length`
- `0 <= times[i] <= 10^9`
- `times` is sorted in a strictly increasing order.
- `times[0] <= t <= 10^9`
- At most `10^4` calls will be made to `q`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 911 Online Election neetcode](https://www.youtube.com/results?search_query=leetcode+911+Online+Election+neetcode)

## Approach

### Intuition

The leading candidate after each vote remains the leader until another candidate passes or ties its count.

### Brute Force

For every query, count all votes up to its time and find the most recent leader.

### Optimal

Precompute the leader at each vote time and binary-search the last vote not later than the query.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), q O(n) | O(n) |
| Optimal | construction O(n), q O(log n) | O(n) |

### Edge cases

- A vote tied for the maximum makes that voter the current leader.
- Queries occur at or after the first vote time.
