# 112. Path Sum

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Palo Alto Networks, Apple, Microsoft, Bloomberg, Amazon, Goldman Sachs, Google, Meta  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/path-sum/](https://leetcode.com/problems/path-sum/)

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```

**Input:** root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
**Output:** true
**Explanation:** The root-to-leaf path with the target sum is shown.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```

**Input:** root = [1,2,3], targetSum = 5
**Output:** false
**Explanation:** There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

**Example 3:**

```

**Input:** root = [], targetSum = 0
**Output:** false
**Explanation:** Since the tree is empty, there are no root-to-leaf paths.

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Video Explanation

[Path Sum - Leetcode 112 - Python](https://www.youtube.com/watch?v=LSKQyOz_P8I)

## Approach

### Intuition

A root-to-leaf path qualifies when its node values sum to targetSum and it ends at a node with no children.

### Brute Force

Enumerate every root-to-leaf path, store its values, and sum each completed path.

### Optimal

Subtract each visited node value from the remaining target and recurse until a leaf is reached.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(nh) |
| Optimal | O(n) | O(h) |

### Edge cases

- A matching sum at an internal node is not enough.
- Negative values are allowed and cannot be pruned by sum size.
- An empty tree has no qualifying path.
