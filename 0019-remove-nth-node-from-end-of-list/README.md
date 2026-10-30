# 19. Remove Nth Node From End of List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Problem

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```

**Input:** head = [1,2,3,4,5], n = 2
**Output:** [1,2,3,5]

```

**Example 2:**

```

**Input:** head = [1], n = 1
**Output:** []

```

**Example 3:**

```

**Input:** head = [1,2], n = 1
**Output:** [1]

```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

## Video Explanation

[Remove Nth Node from End of List - Oracle Interview Question - Leetcode 19](https://www.youtube.com/watch?v=XVuQxVej6y8)

## Approach

### Intuition

Two pointers separated by n nodes reach the target predecessor when the fast pointer reaches the end.

### Brute Force

Count nodes, convert the position from the end to an index from the start, then remove that node.

### Optimal

Start both pointers at a dummy node, advance fast n steps, then move both until fast reaches the tail and bypass slow.next.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- Removing the head is handled by the dummy predecessor.
- A one-node list removed with n=1 returns None.
- Advance fast exactly n nodes so slow stops immediately before the target.
