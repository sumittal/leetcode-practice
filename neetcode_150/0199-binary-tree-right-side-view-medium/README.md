# 199. Binary Tree Right Side View

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/binary-tree-right-side-view/](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Example 1:**

**Input:** root = [1,2,3,null,5,null,4]

**Output:** [1,3,4]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

**Example 2:**

**Input:** root = [1,2,3,4,null,null,null,5]

**Output:** [1,3,4,5]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

**Example 3:**

**Input:** root = [1,null,3]

**Output:** [1,3]

**Example 4:**

**Input:** root = []

**Output:** []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Video Explanation

[Binary Tree Right Side View - Breadth First Search - Leetcode 199](https://www.youtube.com/watch?v=d4zLyf32e3I)

## Approach

### Intuition

The visible value at each depth is the last node visited at that level from left to right.

### Brute Force

For every depth, search all nodes at that depth and select the rightmost one.

### Optimal

Traverse level by level with a queue and record the final node in each level.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nh) | O(h) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty tree has an empty right-side view.
- A right-skewed tree shows every node.
