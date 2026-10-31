# 637. Average of Levels in Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Meta, Amazon, Google, Bloomberg  
**Pattern:** Tree  
**LeetCode:** [https://leetcode.com/problems/average-of-levels-in-binary-tree/](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

## Problem

Given the `root` of a binary tree, return *the average value of the nodes on each level in the form of an array*. Answers within `10^-5` of the actual answer will be accepted.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```

**Input:** root = [3,9,20,15,7]
**Output:** [3.00000,14.50000,11.00000]

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Video Explanation

[YouTube search: Search YouTube for leetcode 637 Average of Levels in Binary Tree neetcode](https://www.youtube.com/results?search_query=leetcode+637+Average+of+Levels+in+Binary+Tree+neetcode)

## Approach

### Intuition

A breadth-first traversal groups nodes by depth, allowing each level's sum to be divided by its node count.

### Brute Force

For each depth, traverse the whole tree and collect nodes at that depth.

### Optimal

Process a queue one level-sized batch at a time and compute its average.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nh) | O(n) |
| Optimal | O(n) | O(w) |

### Edge cases

- A single-node tree has one average equal to its root value.
- The final level may contain only one node.
- Use floating-point division for level means.
