# 105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Problem

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```

**Input:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
**Output:** [3,9,20,null,null,15,7]

```

**Example 2:**

```

**Input:** preorder = [-1], inorder = [-1]
**Output:** [-1]

```

**Constraints:**

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.

## Video Explanation

[Construct Binary Tree from Inorder and Preorder Traversal - Leetcode 105 - Python](https://www.youtube.com/watch?v=ihj4IQGZ2zc)

## Approach

### Intuition

Preorder identifies each subtree root; inorder divides that subtree into left and right portions.

### Brute Force

Search the inorder slice for each root and recursively copy slices.

### Optimal

Use an inorder index map and a shared preorder cursor to build bounded subtrees.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n^2) |
| Optimal | O(n) | O(n) |

### Edge cases

- A single value is both the root and the only inorder element.
- Empty slices represent missing children.
