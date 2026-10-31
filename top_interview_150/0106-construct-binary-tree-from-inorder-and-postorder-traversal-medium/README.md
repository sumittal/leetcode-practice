# 106. Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree  
**Companies:** Walmart Labs, Microsoft, TikTok, Google, Amazon, Bloomberg, Meta  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Problem

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```

**Input:** inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
**Output:** [3,9,20,null,null,15,7]

```

**Example 2:**

```

**Input:** inorder = [-1], postorder = [-1]
**Output:** [-1]

```

**Constraints:**

- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
- `postorder` is **guaranteed** to be the postorder traversal of the tree.

## Video Explanation

[Construct Binary Tree from Inorder and Postorder Traversal - Leetcode 106 - Python](https://www.youtube.com/watch?v=vm63HuIU7kw)

## Approach

### Intuition

The final unused postorder value is the root, and its inorder position separates the left and right subtrees.

### Brute Force

Search each inorder slice for the root and repeatedly create traversal slices for recursive subtrees.

### Optimal

Index inorder positions in a map and consume postorder backward, constructing right subtrees before left subtrees.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n^2) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty traversal pair yields an empty tree.
- Node values are unique, so each inorder split is unambiguous.
- Building right before left follows reverse postorder consumption.
