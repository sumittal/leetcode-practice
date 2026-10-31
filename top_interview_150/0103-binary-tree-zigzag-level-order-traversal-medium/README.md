# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium  
**Tags:** Tree, Breadth-First Search, Binary Tree  
**Companies:** Sigmoid, Nutanix, Adobe, Citadel, Microsoft, Amazon, Walmart Labs, Oracle, Palo Alto Networks, Bloomberg, ByteDance, LinkedIn, Yandex, Google, Meta (+3 more)  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Problem

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[20,9],[15,7]]

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
- `-100 <= Node.val <= 100`

## Video Explanation

[Binary Tree Zigzag Level Order Traversal - Leetcode 103 - Python](https://www.youtube.com/watch?v=igbboQbiwqw)

## Approach

### Intuition

Breadth-first traversal finds each level in order; alternate levels can write values from opposite ends of a result row.

### Brute Force

Collect a normal level-order traversal, then reverse every other level afterward.

### Optimal

Process one queue level at a time and place each value at its forward or reversed index.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(w) |

### Edge cases

- An empty tree returns no levels.
- The root level is left-to-right.
- A singleton level is unchanged by reversal.
