# 543. Diameter of Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Binary Tree, DP on Trees  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)

## Problem

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```

**Input:** root = [1,2,3,4,5]
**Output:** 3
**Explanation:** 3 is the length of the path [4,2,1,3] or [5,2,1,3].

```

**Example 2:**

```

**Input:** root = [1,2]
**Output:** 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Video Explanation

[Diameter of a Binary Tree - Leetcode 543 - Python](https://www.youtube.com/watch?v=bkxqA8Rfv04)

## Approach

### Intuition

At each node, the longest path turning there is the sum of its left and right subtree heights.

### Brute Force

For every node, recompute both subtree heights and maximize their sum.

### Optimal

Compute height once per node with postorder recursion while updating the best diameter in edges.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- A single-node tree has diameter zero.
- A skewed tree's diameter is its number of edges.
