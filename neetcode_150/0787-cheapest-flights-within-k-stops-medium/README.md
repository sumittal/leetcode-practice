# 787. Cheapest Flights Within K Stops

**Difficulty:** Medium  
**Tags:** Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path  
**Pattern:** Advanced Graphs  
**LeetCode:** [https://leetcode.com/problems/cheapest-flights-within-k-stops/](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Problem

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]` indicates that there is a flight from city `from<sub>i</sub>` to city `to<sub>i</sub>` with cost `price<sub>i</sub>`.

You are also given three integers `src`, `dst`, and `k`, return ***the cheapest price** from* `src`* to* `dst`* with at most* `k`* stops.* If there is no such route, return** `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

```

**Input:** n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
**Output:** 700
**Explanation:**
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)

```

**Input:** n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
**Output:** 200
**Explanation:**
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)

```

**Input:** n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
**Output:** 500
**Explanation:**
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

```

**Constraints:**

- `2 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from<sub>i</sub>, to<sub>i</sub> < n`
- `from<sub>i</sub> != to<sub>i</sub>`
- `1 <= price<sub>i</sub> <= 10^4`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Video Explanation

[Bellman-Ford - Cheapest Flights within K Stops - Leetcode 787 - Python](https://www.youtube.com/watch?v=5eIK3zUdYmE)

## Approach

### Intuition

At most k stops permits at most k + 1 flight edges, so relax routes one edge-depth at a time.

### Brute Force

Enumerate every flight route within the edge limit and choose the cheapest destination route.

### Optimal

Apply Bellman-Ford for k + 1 rounds using a snapshot of the previous round's distances.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(V^k) | O(V) |
| Optimal | O(kE) | O(V) |

### Edge cases

- The destination may be unreachable within the allowed stops.
- Using more stops can reduce cost, so the edge limit must be respected.
