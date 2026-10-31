# 114. Flatten Binary Tree to Linked List

**Difficulty:** Medium  
**Tags:** Linked List, Stack, Tree, Depth-First Search, Binary Tree  
**Companies:** josh technology, Microsoft, Bloomberg, Amazon, Meta, Google, Oracle  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/flatten-binary-tree-to-linked-list/](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Problem

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **pre-order**** traversal** of the binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

```

**Input:** root = [1,2,5,3,4,null,6]
**Output:** [1,null,2,null,3,null,4,null,5,null,6]

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Example 3:**

```

**Input:** root = [0]
**Output:** [0]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

## Video Explanation

[YouTube search: Search YouTube for leetcode 114 Flatten Binary Tree to Linked List neetcode](https://www.youtube.com/results?search_query=leetcode+114+Flatten+Binary+Tree+to+Linked+List+neetcode)

## Approach

### Intuition

The required chain follows preorder, so a left subtree must be moved before the original right subtree.

### Brute Force

Collect preorder nodes in an array, then reconnect each node to the next array entry.

### Optimal

For each node with a left child, splice the left subtree's rightmost predecessor before the original right subtree.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The tree may have no left children and already be flattened.
- The original right subtree must be preserved before relinking.
- All left pointers in the final structure must be None.
