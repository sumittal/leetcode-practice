# 235. Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor  
**Companies:** X, BlackRock, LinkedIn, Meta, Amazon, Bloomberg, Microsoft, Atlassian, Yandex, Google  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Problem

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
**Output:** 6
**Explanation:** The LCA of nodes 2 and 8 is 6.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
**Output:** 2
**Explanation:** The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```

**Input:** root = [2,1], p = 2, q = 1
**Output:** 2

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

## Video Explanation

[Lowest Common Ancestor of a Binary Search Tree - Leetcode 235 - Python](https://www.youtube.com/watch?v=gs2LMfuOR9k)

## Approach

### Intuition

In a BST, the first node whose value lies between the two targets is where their paths split.

### Brute Force

Build both root-to-target paths and return their last shared node.

### Optimal

Walk left when both targets are smaller, right when both are larger, otherwise return the current split node.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(h) | O(h) |
| Optimal | O(h) | O(1) |

### Edge cases

- One target may be the ancestor of the other.
- The targets may lie on opposite sides of the root.
