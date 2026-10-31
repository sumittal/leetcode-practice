# 117. Populating Next Right Pointers in Each Node II

**Difficulty:** Medium  
**Tags:** Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Companies:** Bloomberg, Meta, Microsoft, Snowflake, Amazon, Uber, Google  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Problem

Given a binary tree

```

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

```

**Input:** root = [1,2,3,4,5,null,7]
**Output:** [1,#,2,3,#,4,5,7,#]
**Explanation: **Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 6000]`.
- `-100 <= Node.val <= 100`

**Follow-up:**

- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Video Explanation

[YouTube search: Search YouTube for leetcode 117 Populating Next Right Pointers in Each Node II neetcode](https://www.youtube.com/results?search_query=leetcode+117+Populating+Next+Right+Pointers+in+Each+Node+II+neetcode)

## Approach

### Intuition

The next level can be linked while traversing the current level through its already-established next pointers.

### Brute Force

Run breadth-first search with a queue and connect adjacent nodes in each level.

### Optimal

Use a dummy head and tail to stitch each next level in one pass, reusing the current level's next chain.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The tree may be sparse and need not be perfect.
- The final node on every level must point to None.
- An empty tree returns None.
