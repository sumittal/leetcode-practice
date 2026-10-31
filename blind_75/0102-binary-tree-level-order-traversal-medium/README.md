# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Tags:** Tree, Breadth-First Search, Binary Tree  
**Companies:** Palo Alto Networks, Bloomberg, Apple, Amazon, Microsoft, Meta, josh technology, LinkedIn, Oracle, Adobe, Google, Visa, Yandex, TikTok, Goldman Sachs  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Problem

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

```

**Example 2:**

```

**Input:** root = [1]
**Output:** [[1]]

```

**Example 3:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Video Explanation

[Binary Tree Level Order Traversal - BFS - Leetcode 102](https://www.youtube.com/watch?v=6ZnyEApgFYg)

## Approach

### Intuition

A FIFO queue visits nodes in the same order they appear by depth.

### Brute Force

For each depth, recursively collect nodes whose depth matches it.

### Optimal

Process exactly the queue size at each level, collecting values before enqueuing children.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n*h) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty tree has no levels.
- A single node forms one one-element level.
