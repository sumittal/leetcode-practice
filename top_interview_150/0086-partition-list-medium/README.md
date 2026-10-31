# 86. Partition List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers  
**Companies:** Amazon, Bloomberg, Google, Meta, Microsoft  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/partition-list/](https://leetcode.com/problems/partition-list/)

## Problem

Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

```

**Input:** head = [1,4,3,2,5,2], x = 3
**Output:** [1,2,2,4,3,5]

```

**Example 2:**

```

**Input:** head = [2,1], x = 2
**Output:** [1,2]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Video Explanation

[Partition List - Linked List - Leetcode 86](https://www.youtube.com/watch?v=KT1iUciJr4g)

## Approach

### Intuition

Stable partitioning requires preserving the original relative order in both the less-than-x and greater-or-equal groups.

### Brute Force

Copy values into two arrays by comparison with x, concatenate them, and rebuild a list.

### Optimal

Append original nodes to two separate linked lists and connect the less-than list to the other list.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- Either partition can be empty.
- Nodes equal to x belong in the second partition.
- The second tail must be terminated to prevent a stale link or cycle.
