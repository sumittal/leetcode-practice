# 124. Binary Tree Maximum Path Sum

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees  
**Companies:** Baidu, DoorDash, Wix, Nutanix, Adobe, Citadel, Amazon, TikTok, Datadog, Salesforce, Meta, Yandex, Microsoft, Bloomberg, Google (+9 more)  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/binary-tree-maximum-path-sum/](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Problem

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```

**Input:** root = [1,2,3]
**Output:** 6
**Explanation:** The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```

**Input:** root = [-10,9,20,null,null,15,7]
**Output:** 42
**Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

## Video Explanation

[Binary Tree Maximum Path Sum - DFS - Leetcode 124 - Python](https://www.youtube.com/watch?v=Hr5cWUld4vU)

## Approach

### Intuition

A path may turn at one node, but a parent can extend through only one child branch.

### Brute Force

Enumerate every node pair and compute the path between them.

### Optimal

Postorder returns the best downward gain and updates a global best with both positive child gains.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- Ignore negative child gains when extending a path.
- The best path may be a single negative node.
