# 226. Invert Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Palo Alto Networks, josh technology, Amazon, Google, Microsoft, Meta, LinkedIn, Oracle, Bloomberg  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/invert-binary-tree/](https://leetcode.com/problems/invert-binary-tree/)

## Problem

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```

**Input:** root = [2,1,3]
**Output:** [2,3,1]

```

**Example 3:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Video Explanation

[Invert Binary Tree - Depth First Search - Leetcode 226](https://www.youtube.com/watch?v=OnSn2XEQ4MY)

## Approach

### Intuition

Inverting a tree swaps the left and right child at every node.

### Brute Force

Collect nodes by level and rebuild a tree with each level reversed.

### Optimal

Recursively invert both subtrees and swap the returned children at each node.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(h) recursion stack |

### Edge cases

- An empty tree remains None.
- A leaf has no children to swap.
- Swap the child references at every visited node, not just at the root.
