# 1586. Binary Search Tree Iterator II

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator  
**Companies:** Meta  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/binary-search-tree-iterator-ii/](https://leetcode.com/problems/binary-search-tree-iterator-ii/)

## Problem

Create a BST iterator that can move forward and backward through inorder values. Example 1: for a tree with inorder [3, 7, 9, 15, 20], next returns 3 then 7, and prev returns 3. Example 2: after moving to the last element, hasNext is false while hasPrev remains true. Constraints: the tree is nonempty and all keys are unique.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1586 Binary Search Tree Iterator II neetcode](https://www.youtube.com/results?search_query=leetcode+1586+Binary+Search+Tree+Iterator+II+neetcode)

## Approach

### Intuition

Materializing the inorder sequence turns bidirectional iteration into cursor movement.

### Brute Force

Recompute inorder traversal from the root for each next or prev operation.

### Optimal

Build one inorder list and maintain the index of the current element.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | next/prev O(n), construction O(1) | O(h) |
| Optimal | construction O(n), next/prev/hasNext/hasPrev O(1) | O(n) |

### Edge cases

- The cursor begins before the first value.
- prev is only called when hasPrev is true.
