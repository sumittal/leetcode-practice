# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor  
**Companies:** Airwallex, Wix, Meta, Atlassian, Amazon, Adobe, Lucid, BitGo, LinkedIn, SAP, Apple, BlackRock, Yandex, Microsoft, TikTok (+6 more)  
**Pattern:** Tree  
**LeetCode:** [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Output:** 3
**Explanation:** The LCA of nodes 5 and 1 is 3.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**Output:** 5
**Explanation:** The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```

**Input:** root = [1,2], p = 1, q = 2
**Output:** 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Video Explanation

[YouTube search: Search YouTube for leetcode 236 Lowest Common Ancestor of a Binary Tree neetcode](https://www.youtube.com/results?search_query=leetcode+236+Lowest+Common+Ancestor+of+a+Binary+Tree+neetcode)

## Approach

### Intuition

The lowest common ancestor is the first node whose subtree contains both target nodes, including the case where one target is that node.

### Brute Force

For each node, search both subtrees for both targets and keep the deepest node containing them.

### Optimal

Return a target when found, combine non-null results from both children, and otherwise propagate the one found result upward.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- The ancestor may be one of the target nodes.
- Targets can lie in separate child subtrees.
- The test must pass the actual nodes from the constructed tree.
