# 3391. Design a 3D Binary Matrix with Efficient Layer Tracking

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Design, Heap (Priority Queue), Matrix, Ordered Set  
**Companies:** Amdocs  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/](https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/)

## Problem

Maintain an n by n by n binary matrix and support setting or clearing a cell. Query the layer index containing the most ones; ties go to the largest layer index. Example 1: in a three-layer matrix, setting two cells in layer 0 and one in layer 2 makes largestMatrix return 0. Example 2: when all layers contain zero ones, the tie rule returns n - 1. Constraints: 1 <= n <= 100, coordinates are in range, and there are at most 100000 updates and 10000 queries.

## Video Explanation

[YouTube search: Search YouTube for leetcode 3391 Design a 3D Binary Matrix with Efficient Layer Tracking neetcode](https://www.youtube.com/results?search_query=leetcode+3391+Design+a+3D+Binary+Matrix+with+Efficient+Layer+Tracking+neetcode)

## Approach

### Intuition

Only the count for the changed layer can move, and a priority queue can expose the highest count with the required index tie-break.

### Brute Force

Store all cells, then scan every layer and count its ones for every query.

### Optimal

Store each layer as bytes, maintain its one-count, and lazily validate a heap ordered by count descending and layer descending.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | set/unset O(1), largestMatrix O(n^3) | O(n^3) |
| Optimal | setCell/unsetCell O(log q), largestMatrix O(1) amortized | O(n^3 + q) |

### Edge cases

- Setting an already-set cell or clearing an already-clear cell must not change a count.
- The largest layer index wins ties, including the all-zero initial state.
