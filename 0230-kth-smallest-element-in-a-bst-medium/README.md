# 230. Kth Smallest Element in a BST

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/kth-smallest-element-in-a-bst/](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem

Given the `root` of a binary search tree, and an integer `k`, return *the* `k^th` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```

**Input:** root = [3,1,4,null,2], k = 1
**Output:** 1

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```

**Input:** root = [5,3,6,2,4,null,null,1], k = 3
**Output:** 3

```

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Video Explanation

[Kth Smallest Element in a BST - Leetcode 230 - Python](https://www.youtube.com/watch?v=5LUXSvjmGCw)

## Approach

### Intuition

Inorder traversal of a BST visits values in increasing order.

### Brute Force

Traverse and sort all node values, then select index k-1.

### Optimal

Iterative inorder traversal stops when the kth node is popped.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(h+k) | O(h) |

### Edge cases

- k=1 returns the minimum.
- Stop at the kth visit without traversing the remaining tree.
