# 431. Encode N-ary Tree to Binary Tree

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree  
**Companies:** None reported  
**Pattern:** Tree  
**LeetCode:** [https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/)

## Problem

Convert an N-ary tree to a binary tree and back without losing values or child order. In the binary form, a node's left pointer leads to its first child and right pointers link siblings. Example 1: a root with children 3, 2, and 4, where node 3 has children 5 and 6, must decode to the same ordered tree. Example 2: a single-node tree remains a single node after a round trip. Constraints: node values are unique, there are at most 1000 nodes, and the N-ary tree has no more than 10 children per node.

## Video Explanation

[YouTube search: Search YouTube for leetcode 431 Encode N-ary Tree to Binary Tree neetcode](https://www.youtube.com/results?search_query=leetcode+431+Encode+N-ary+Tree+to+Binary+Tree+neetcode)

## Approach

### Intuition

Left-child/right-sibling encoding stores each ordered child list as one left edge followed by a right-linked sibling chain.

### Brute Force

Serialize the entire N-ary tree into a separate nested representation and rebuild it during decoding.

### Optimal

Recursively map each node's first child to left and each later sibling to the previous child's right pointer.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | encode/decode O(n) | O(n) |
| Optimal | encode/decode O(n) | O(h) recursion plus O(n) output tree |

### Edge cases

- A leaf has no left child.
- Child order must remain unchanged through both conversions.
