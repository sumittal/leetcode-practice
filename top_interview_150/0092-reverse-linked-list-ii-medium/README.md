# 92. Reverse Linked List II

**Difficulty:** Medium  
**Tags:** Linked List  
**Companies:** Revolut, Nutanix, Arista Networks, Palo Alto Networks, ByteDance, Nvidia, Infosys, Amazon, Bloomberg, Microsoft, Google, Meta, Oracle, TikTok, Apple  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)

## Problem

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```

**Input:** head = [1,2,3,4,5], left = 2, right = 4
**Output:** [1,4,3,2,5]

```

**Example 2:**

```

**Input:** head = [5], left = 1, right = 1
**Output:** [5]

```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

**Follow up:** Could you do it in one pass?

## Video Explanation

[Reverse Linked List II - Leetcode 92 - Python](https://www.youtube.com/watch?v=RF_M9tX4Eag)

## Approach

### Intuition

Only the nodes between left and right need their links reversed; the surrounding list can reconnect at the segment boundaries.

### Brute Force

Copy the list values, reverse the selected slice, and rebuild a new list.

### Optimal

Repeatedly move the node after the segment head to the segment's front using head insertion.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The selected segment may begin at the head.
- A one-node segment is unchanged.
- All nodes may be included in the reversed segment.
