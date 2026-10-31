# 1448. Count Good Nodes in Binary Tree

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/count-good-nodes-in-binary-tree/](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Problem

Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.

Return the number of **good** nodes in the binary tree.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)**

```

**Input:** root = [3,1,4,3,null,1,5]
**Output:** 4
**Explanation:** Nodes in blue are **good**.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

**Example 2:**

**![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)**

```

**Input:** root = [3,3,null,4,2]
**Output:** 3
**Explanation:** Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

**Example 3:**

```

**Input:** root = [1]
**Output:** 1
**Explanation:** Root is considered as **good**.
```

**Constraints:**

- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

## Video Explanation

[Microsoft's Most Asked Question 2021 - Count Good Nodes in a Binary Tree - Leetcode 1448 - Python](https://www.youtube.com/watch?v=7cp5imvDzl4)

## Approach

### Intuition

A node is good when no larger value appears on the path from the root to that node.

### Brute Force

For each node, walk back to the root and find the maximum value on its path.

### Optimal

Traverse once while carrying the maximum value seen on the current root-to-node path.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nh) | O(h) |
| Optimal | O(n) | O(h) |

### Edge cases

- The root is always good.
- Equal values to the path maximum count as good.
