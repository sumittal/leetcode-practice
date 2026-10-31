# 1724. Checking Existence of Edge Length Limited Paths II

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Depth-First Search, Union-Find, Graph Theory, Design, Sorting, Heap (Priority Queue), Minimum Spanning Tree  
**Companies:** Google  
**Pattern:** Depth-First Search  
**LeetCode:** [https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/)

## Problem

Preprocess a weighted undirected graph so queries can test whether two vertices are connected using only edges strictly below a limit. Example 1: with edges 0-1 of weight 2 and 1-2 of weight 5, query(0,2,6) is true. Example 2: query(0,2,5) is false because the weight-5 edge is not strictly below the limit. Constraints: the graph has up to 10^5 vertices and edges, and paths are undirected.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1724 Checking Existence of Edge Length Limited Paths II neetcode](https://www.youtube.com/results?search_query=leetcode+1724+Checking+Existence+of+Edge+Length+Limited+Paths+II+neetcode)

## Approach

### Intuition

A minimum spanning forest preserves the minimum possible bottleneck between every connected pair.

### Brute Force

Run a limited-edge graph search for every query.

### Optimal

Build a minimum spanning forest, preprocess binary-lifting ancestors with maximum edge weights, and test the path bottleneck.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | query O(n + m) | O(n + m) |
| Optimal | construction O(m log m + n log n), query O(log n) | O(n log n + m) |

### Edge cases

- A vertex is connected to itself by an empty path.
- An edge equal to the limit is not allowed in the path.
