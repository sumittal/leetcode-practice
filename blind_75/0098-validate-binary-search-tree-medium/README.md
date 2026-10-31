# 98. Validate Binary Search Tree

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree  
**Companies:** Wix, Millennium, Bloomberg, Asana, Yahoo, Microsoft, Amazon, Expedia, Lyft, Meta, Citadel, Oracle, Google, Salesforce, IBM (+4 more)  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/validate-binary-search-tree/](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```

**Input:** root = [2,1,3]
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Video Explanation

[Validate Binary Search Tree - Depth First Search - Leetcode 98](https://www.youtube.com/watch?v=s6ATEkipzow)

## Approach

### Intuition

Each node must satisfy every ancestor bound, not merely compare correctly with its immediate children.

### Brute Force

Check each node against all values in its left and right subtrees.

### Optimal

Propagate exclusive lower and upper bounds down the tree.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- Duplicate values violate strict BST ordering.
- A locally plausible child can still violate a distant ancestor bound.
