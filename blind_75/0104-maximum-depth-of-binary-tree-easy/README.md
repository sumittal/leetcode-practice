# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Yahoo, Arista Networks, Avito, LinkedIn, Qualcomm, Microsoft, Spotify, Uber, Apple, Bloomberg, Amazon, Accenture, Zoho, Google, Infosys (+3 more)  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 3

```

**Example 2:**

```

**Input:** root = [1,null,2]
**Output:** 2

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Video Explanation

[Maximum Depth of Binary Tree - 3 Solutions - Leetcode 104 - Python](https://www.youtube.com/watch?v=hTM3phVI6YQ)

## Approach

### Intuition

A nonempty tree's depth is one plus the larger depth of its left and right subtrees.

### Brute Force

Traverse each root-to-leaf path and record the greatest path length.

### Optimal

Recursively compute both subtree depths and return one plus their maximum.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(h) |
| Optimal | O(n) | O(h) recursion stack |

### Edge cases

- An empty tree has depth zero.
- A single node has depth one.
- A missing child contributes depth zero.
