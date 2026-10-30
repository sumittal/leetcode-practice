# 297. Serialize and Deserialize Binary Tree

**Difficulty:** Hard  
**Tags:** String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/serialize-and-deserialize-binary-tree/](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Problem

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```

**Input:** root = [1,2,3,null,null,4,5]
**Output:** [1,2,3,null,null,4,5]

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`

## Video Explanation

[Serialize and Deserialize Binary Tree - Preorder Traversal - Leetcode 297 - Python](https://www.youtube.com/watch?v=u4JAi2JJhI8)

## Approach

### Intuition

A traversal with explicit null markers uniquely captures both node values and shape.

### Brute Force

Serialize a level-order array with placeholders and parse it back.

### Optimal

Use preorder tokens including null markers; consume them recursively in the same order.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty tree must serialize and deserialize consistently.
- Skewed trees require preserving every missing-child marker.
