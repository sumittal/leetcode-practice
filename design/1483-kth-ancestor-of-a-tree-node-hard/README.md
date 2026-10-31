# 1483. Kth Ancestor of a Tree Node

**Difficulty:** Hard  
**Tags:** Binary Search, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Design, Binary Lifting  
**Companies:** Google, Goldman Sachs, Bloomberg, Amazon  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/kth-ancestor-of-a-tree-node/](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)

## Problem

You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of `i^th` node. The root of the tree is node `0`. Find the `k^th` ancestor of a given node.

The `k^th` ancestor of a tree node is the `k^th` node in the path from that node to the root node.

Implement the `TreeAncestor` class:

- `TreeAncestor(int n, int[] parent)` Initializes the object with the number of nodes in the tree and the parent array.
- `int getKthAncestor(int node, int k)` return the `k^th` ancestor of the given node `node`. If there is no such ancestor, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/08/28/1528_ex1.png)

```

**Input**
["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
**Output**
[null, 1, 0, -1]

**Explanation**
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
```

**Constraints:**

- `1 <= k <= n <= 5 * 10^4`
- `parent.length == n`
- `parent[0] == -1`
- `0 <= parent[i] < n` for all `0 < i < n`
- `0 <= node < n`
- There will be at most `5 * 10^4` queries.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1483 Kth Ancestor of a Tree Node neetcode](https://www.youtube.com/results?search_query=leetcode+1483+Kth+Ancestor+of+a+Tree+Node+neetcode)

## Approach

### Intuition

Repeated parent jumps can be composed into powers of two.

### Brute Force

Follow the parent pointer once for every requested ancestor step.

### Optimal

Precompute binary-lifting ancestors and combine entries for the set bits of k.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), getKthAncestor O(k) | O(n) |
| Optimal | construction O(n log n), getKthAncestor O(log n) | O(n log n) |

### Edge cases

- A missing parent remains -1 through all higher jumps.
- k equal to zero returns the queried node.
