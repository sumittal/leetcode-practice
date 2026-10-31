# 25. Reverse Nodes in k-Group

**Difficulty:** Hard  
**Tags:** Linked List, Recursion  
**Companies:** Qualcomm, Cadence, Sigmoid, Arista Networks, ZScaler, Microsoft, Autodesk, TikTok, josh technology, Zopsmart, MathWorks, Amazon, Salesforce, Palo Alto Networks, Bloomberg (+9 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/reverse-nodes-in-k-group/](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```

**Input:** head = [1,2,3,4,5], k = 2
**Output:** [2,1,4,3,5]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```

**Input:** head = [1,2,3,4,5], k = 3
**Output:** [3,2,1,4,5]

```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?

## Video Explanation

[Reverse Nodes in K-Group - Linked List - Leetcode 25](https://www.youtube.com/watch?v=1UOPsfP85V4)

## Approach

### Intuition

Reverse only complete blocks of k nodes; an incomplete suffix must remain in its original order.

### Brute Force

Collect values in groups, reverse each complete group, and construct a new list.

### Optimal

Check that a full group exists, reverse its links in place, and connect its new head and tail to adjacent groups.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A list shorter than k remains unchanged.
- The last group is left untouched when it has fewer than k nodes.
