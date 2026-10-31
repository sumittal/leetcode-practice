# 141. Linked List Cycle

**Difficulty:** Easy  
**Tags:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

## Problem

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true`* if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```

**Input:** head = [3,2,0,-4], pos = 1
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```

**Input:** head = [1,2], pos = 0
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```

**Input:** head = [1], pos = -1
**Output:** false
**Explanation:** There is no cycle in the linked list.

```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Video Explanation

[Linked List Cycle - Floyd's Tortoise and Hare - Leetcode 141 - Python](https://www.youtube.com/watch?v=gBTe7lFR3vc)

## Approach

### Intuition

If traversal enters a cycle, a faster pointer eventually laps a slower pointer.

### Brute Force

Track visited node identities and return true when a node is visited twice.

### Optimal

Advance slow by one link and fast by two; equality of node identity proves a cycle.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- An empty list or a single node without a self-link has no cycle.
- Compare node identity, not node values.
- Check fast and fast.next before advancing two steps.
