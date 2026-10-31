# 530. Minimum Absolute Difference in BST

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree  
**Companies:** Google, Meta, Amazon  
**Pattern:** Tree  
**LeetCode:** [https://leetcode.com/problems/minimum-absolute-difference-in-bst/](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Problem

Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)

```

**Input:** root = [4,2,6,1,3]
**Output:** 1

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)

```

**Input:** root = [1,0,48,null,null,12,49]
**Output:** 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 10^4]`.
- `0 <= Node.val <= 10^5`

**Note:** This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

## Video Explanation

[YouTube search: Search YouTube for leetcode 530 Minimum Absolute Difference in BST neetcode](https://www.youtube.com/results?search_query=leetcode+530+Minimum+Absolute+Difference+in+BST+neetcode)

## Approach

### Intuition

Inorder traversal of a BST visits values in sorted order, so the minimum difference must occur between adjacent visited values.

### Brute Force

Collect all values and compare every pair to find the smallest absolute difference.

### Optimal

Traverse inorder iteratively and compare each value only with its predecessor.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(h) |

### Edge cases

- At least two nodes are provided.
- The smallest difference is between adjacent sorted values.
- Do not compare a node with a missing predecessor.
