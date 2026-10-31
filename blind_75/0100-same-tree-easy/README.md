# 100. Same Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Bloomberg, Amazon, Google, Microsoft, Meta, tcs, LinkedIn, Apple, Oracle  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/same-tree/](https://leetcode.com/problems/same-tree/)

## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```

**Input:** p = [1,2,3], q = [1,2,3]
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```

**Input:** p = [1,2], q = [1,null,2]
**Output:** false

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```

**Input:** p = [1,2,1], q = [1,1,2]
**Output:** false

```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Video Explanation

[Same Tree - Leetcode 100 - Python](https://www.youtube.com/watch?v=vRbbcKXCxOw)

## Approach

### Intuition

Two trees match only when corresponding nodes agree and their left and right subtrees also match.

### Brute Force

Serialize both trees with explicit null markers and compare the encodings.

### Optimal

Recursively compare paired nodes, values, and corresponding children.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n+m) | O(n+m) |
| Optimal | O(min(n,m)) | O(h) |

### Edge cases

- Two empty trees are equal.
- One missing node or one unequal value makes the trees different.
