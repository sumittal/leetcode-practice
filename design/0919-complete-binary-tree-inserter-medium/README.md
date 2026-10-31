# 919. Complete Binary Tree Inserter

**Difficulty:** Medium  
**Tags:** Tree, Breadth-First Search, Design, Binary Tree  
**Companies:** Google, Meta  
**Pattern:** Tree  
**LeetCode:** [https://leetcode.com/problems/complete-binary-tree-inserter/](https://leetcode.com/problems/complete-binary-tree-inserter/)

## Problem

A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the `CBTInserter` class:

- `CBTInserter(TreeNode root)` Initializes the data structure with the `root` of the complete binary tree.
- `int insert(int v)` Inserts a `TreeNode` into the tree with value `Node.val == val` so that the tree remains complete, and returns the value of the parent of the inserted `TreeNode`.
- `TreeNode get_root()` Returns the root node of the tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg)

```

**Input**
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
**Output**
[null, 1, 2, [1, 2, 3, 4]]

**Explanation**
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // return 1
cBTInserter.insert(4);  // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]

```

**Constraints:**

- The number of nodes in the tree will be in the range `[1, 1000]`.
- `0 <= Node.val <= 5000`
- `root` is a complete binary tree.
- `0 <= val <= 5000`
- At most `10^4` calls will be made to `insert` and `get_root`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 919 Complete Binary Tree Inserter neetcode](https://www.youtube.com/results?search_query=leetcode+919+Complete+Binary+Tree+Inserter+neetcode)

## Approach

### Intuition

The next insertion point is the earliest level-order node missing a child.

### Brute Force

Search the tree from the root for the first incomplete node on every insertion.

### Optimal

Maintain a queue of nodes with fewer than two children and fill them from the front.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | insert O(n), initialization O(1) | O(1) extra |
| Optimal | insert O(1), initialization O(n) | O(n) |

### Edge cases

- The parent returned by insert is the node that receives the new child.
- The root object remains the same throughout insertions.
