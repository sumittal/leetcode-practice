# 207. Course Schedule

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph  
**Companies:** Zenefits, Nordstrom, Yelp, Coupang, TikTok, Swiggy, ByteDance, Amazon, Snowflake, Cruise, Apple, Anduril, BitGo, LiveRamp, Meta (+28 more)  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that you **must** take course `b<sub>i</sub>` first if you want to take course `a<sub>i</sub>`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**

```

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true
**Explanation:** There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

```

**Example 2:**

```

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
**Output:** false
**Explanation:** There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses`
- All the pairs prerequisites[i] are **unique**.

## Video Explanation

[Course Schedule - Graph Adjacency List - Leetcode 207](https://www.youtube.com/watch?v=EgI5nU9etnU)

## Approach

### Intuition

A schedule exists exactly when prerequisite edges contain no directed cycle.

### Brute Force

Try repeatedly ordering courses and checking every prerequisite.

### Optimal

Kahn's algorithm removes zero-indegree courses and succeeds if all courses are removed.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(V+E) |
| Optimal | O(V+E) | O(V+E) |

### Edge cases

- No prerequisites allows every course.
- A self-dependency forms a cycle.
