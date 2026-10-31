# 108. Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy  
**Tags:** Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree  
**Companies:** Airbnb, Accenture, Amazon, Apple, Microsoft, Google, Meta, TikTok, Bloomberg  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Problem

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a* ***height-balanced*** *binary search tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```

**Input:** nums = [-10,-3,0,5,9]
**Output:** [0,-3,9,-10,null,5]
**Explanation:** [0,-10,5,null,-3,null,9] is also accepted:
![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

```

**Input:** nums = [1,3]
**Output:** [3,1]
**Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a **strictly increasing** order.

## Video Explanation

[Convert Sorted Array to Binary Search Tree - Leetcode 108 - Python](https://www.youtube.com/watch?v=0K0uCMYq5ng)

## Approach

### Intuition

Choose a middle value as each subtree root so both recursive halves stay height-balanced.

### Brute Force

Insert sorted values one at a time into a BST, then rebalance the resulting skewed tree.

### Optimal

Recursively use the middle index and construct the left and right slices as subtrees.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) for plain insertion | O(n) |
| Optimal | O(n) | O(log n) recursion for a balanced result |

### Edge cases

- An empty array produces an empty tree.
- One value becomes the root.
- Several valid balanced shapes are acceptable; compare balance and inorder values.
