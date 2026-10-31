# 449. Serialize and Deserialize BST

**Difficulty:** Medium  
**Tags:** String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree  
**Companies:** Shopee, Amazon, Microsoft, Google  
**Pattern:** String  
**LeetCode:** [https://leetcode.com/problems/serialize-and-deserialize-bst/](https://leetcode.com/problems/serialize-and-deserialize-bst/)

## Problem

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

**The encoded string should be as compact as possible.**

**Example 1:**

```
**Input:** root = [2,1,3]
**Output:** [2,1,3]

```

**Example 2:**

```
**Input:** root = []
**Output:** []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`
- The input tree is **guaranteed** to be a binary search tree.

## Video Explanation

[YouTube search: Search YouTube for leetcode 449 Serialize and Deserialize BST neetcode](https://www.youtube.com/results?search_query=leetcode+449+Serialize+and+Deserialize+BST+neetcode)

## Approach

### Intuition

BST ordering allows a preorder traversal to encode the tree without explicit null markers.

### Brute Force

Serialize every child pointer with null markers, then rebuild the exact shape using generic binary-tree traversal.

### Optimal

Store preorder values and reconstruct by attaching each value to the most recent smaller ancestor; unique BST values preserve the original shape.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | serialize O(n), deserialize O(n) | O(n) |
| Optimal | serialize O(n), deserialize O(n) | O(n) |

### Edge cases

- An empty tree serializes to an empty string.
- A one-sided BST must retain the same shape after decoding.
