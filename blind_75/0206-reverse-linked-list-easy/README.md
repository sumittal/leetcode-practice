# 206. Reverse Linked List

**Difficulty:** Easy  
**Tags:** Linked List, Recursion  
**Companies:** Yahoo, Zenefits, Zynga, Luxoft, Yelp, X, Qualcomm, Nokia, Adobe, Snap, Apple, SAP, Paytm, Microsoft, Oracle (+18 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)

## Problem

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```

**Input:** head = [1,2]
**Output:** [2,1]

```

**Example 3:**

```

**Input:** head = []
**Output:** []

```

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Video Explanation

[Reverse Linked List - Iterative AND Recursive - Leetcode 206 - Python](https://www.youtube.com/watch?v=G0_I-ZF0S38)

## Approach

### Intuition

Reverse each link as the list is traversed, keeping the reversed prefix and the untouched suffix separate.

### Brute Force

Copy node values, reverse the values, and write them back into the nodes.

### Optimal

Iteratively save the next node, point the current node backward, then advance the previous and current pointers. A recursive version uses O(n) call-stack space.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- An empty list remains empty.
- A one-node list already has the required direction.
- Save the original next pointer before reversing the current link.
