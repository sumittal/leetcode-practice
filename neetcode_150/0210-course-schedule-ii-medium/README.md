# 210. Course Schedule II

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that you **must** take course `b<sub>i</sub>` first if you want to take course `a<sub>i</sub>`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

```

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

```

**Example 2:**

```

**Input:** numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
**Output:** [0,2,1,3]
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

```

**Example 3:**

```

**Input:** numCourses = 1, prerequisites = []
**Output:** [0]

```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses`
- `a<sub>i</sub> != b<sub>i</sub>`
- All the pairs `[a<sub>i</sub>, b<sub>i</sub>]` are **distinct**.

## Video Explanation

[Course Schedule II - Topological Sort - Leetcode 210](https://www.youtube.com/watch?v=Akt3glAwyfY)

## Approach

### Intuition

A valid course order is a topological ordering of the prerequisite graph.

### Brute Force

Try permutations of courses and check whether every prerequisite appears first.

### Optimal

Use Kahn's algorithm to repeatedly take courses with zero remaining prerequisites.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(V! + E) | O(V) |
| Optimal | O(V + E) | O(V + E) |

### Edge cases

- A directed cycle makes it impossible to finish all courses.
- Multiple valid topological orders may exist.
