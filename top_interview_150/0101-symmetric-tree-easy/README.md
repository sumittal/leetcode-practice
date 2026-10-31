# 101. Symmetric Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** VK, LinkedIn, Yandex, Bloomberg, EPAM Systems, Microsoft, Amazon, Google, Infosys, Meta  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/symmetric-tree/](https://leetcode.com/problems/symmetric-tree/)

## Problem

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```

**Input:** root = [1,2,2,3,4,4,3]
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```

**Input:** root = [1,2,2,null,3,null,3]
**Output:** false

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

## Video Explanation

[Symmetric Tree - Leetcode 101 - Python](https://www.youtube.com/watch?v=Mao9uzxwvmc)

## Approach

### Intuition

A tree is symmetric when its left and right subtrees are mirror images at every pair of positions.

### Brute Force

Serialize both subtrees with null markers, reverse one serialization, and compare them.

### Optimal

Recursively compare outer children with each other and inner children with each other.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(h) |

### Edge cases

- An empty tree is symmetric.
- A single node is symmetric.
- Matching values alone are insufficient if child positions differ.
