# 222. Count Complete Tree Nodes

**Difficulty:** Medium  
**Tags:** Binary Search, Bit Manipulation, Tree, Binary Tree  
**Companies:** Dunzo, Adobe, Google, Meta, Bloomberg, Amazon, Microsoft  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/count-complete-tree-nodes/](https://leetcode.com/problems/count-complete-tree-nodes/)

## Problem

Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to **Wikipedia**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than `O(n)` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

```

**Input:** root = [1,2,3,4,5,6]
**Output:** 6

```

**Example 2:**

```

**Input:** root = []
**Output:** 0

```

**Example 3:**

```

**Input:** root = [1]
**Output:** 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
- `0 <= Node.val <= 5 * 10^4`
- The tree is guaranteed to be **complete**.

## Video Explanation

[YouTube search: Search YouTube for leetcode 222 Count Complete Tree Nodes neetcode](https://www.youtube.com/results?search_query=leetcode+222+Count+Complete+Tree+Nodes+neetcode)

## Approach

### Intuition

A complete tree is perfect when its leftmost and rightmost heights match; otherwise recurse into its two smaller complete subtrees.

### Brute Force

Traverse every node and increment a counter.

### Optimal

Compare leftmost and rightmost heights; count a perfect subtree with 2^height-1, otherwise recurse.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(h) |
| Optimal | O(log^2 n) | O(log n) |

### Edge cases

- An empty tree has zero nodes.
- A perfect subtree can be counted without visiting each node.
- The height shortcut relies on the complete-tree guarantee.
