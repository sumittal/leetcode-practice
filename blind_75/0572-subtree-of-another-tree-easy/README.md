# 572. Subtree of Another Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, String Matching, Binary Tree, Hash Function  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/subtree-of-another-tree/](https://leetcode.com/problems/subtree-of-another-tree/)

## Problem

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of` subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```

**Input:** root = [3,4,5,1,2], subRoot = [4,1,2]
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```

**Input:** root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
**Output:** false

```

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Video Explanation

[Subtree of Another Tree - Leetcode 572 - Python](https://www.youtube.com/watch?v=E36O5SWp-LE)

## Approach

### Intuition

A subtree match can begin at any node of the main tree, but must match all descendants exactly.

### Brute Force

Serialize both trees with null markers and search one encoding inside the other.

### Optimal

At each main-tree node, test exact structural equality; otherwise search its children.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n+m) | O(n+m) |
| Optimal | O(n*m) | O(h) |

### Edge cases

- An empty candidate tree is a subtree.
- Matching values alone is insufficient when child structure differs.
