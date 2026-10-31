# 110. Balanced Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Binary Tree  
**Companies:** Bloomberg, Amazon, Anduril, Visa, Microsoft, Meta, Google, tcs, Apple  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/balanced-binary-tree/](https://leetcode.com/problems/balanced-binary-tree/)

## Problem

Given a binary tree, determine if it is **height-balanced**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```

**Input:** root = [1,2,2,3,3,null,null,4,4]
**Output:** false

```

**Example 3:**

```

**Input:** root = []
**Output:** true

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Video Explanation

[Balanced Binary Tree - Leetcode 110 - Python](https://www.youtube.com/watch?v=QfJsau0ItOY)

## Approach

### Intuition

A tree is balanced when every subtree is balanced and its child heights differ by at most one.

### Brute Force

For every node, independently compute both subtree heights and compare them.

### Optimal

Return each subtree height bottom-up, using a sentinel value to propagate imbalance immediately.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- An empty tree is balanced.
- A long one-sided chain is unbalanced once its height difference exceeds one.
