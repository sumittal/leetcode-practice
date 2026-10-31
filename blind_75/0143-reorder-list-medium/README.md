# 143. Reorder List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers, Stack, Recursion  
**Companies:** Arista Networks, Bloomberg, Snap, Amazon, Morgan Stanley, TikTok, Microsoft, Meta, tcs, Google, Apple, Infosys, LinkedIn  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/reorder-list/](https://leetcode.com/problems/reorder-list/)

## Problem

You are given the head of a singly linked-list. The list can be represented as:

```

L<sub>0</sub> → L<sub>1</sub> → … → L<sub>n - 1</sub> → L<sub>n</sub>

```

*Reorder the list to be on the following form:*

```

L<sub>0</sub> → L<sub>n</sub> → L<sub>1</sub> → L<sub>n - 1</sub> → L<sub>2</sub> → L<sub>n - 2</sub> → …

```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```

**Input:** head = [1,2,3,4]
**Output:** [1,4,2,3]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

```

**Input:** head = [1,2,3,4,5]
**Output:** [1,5,2,4,3]

```

**Constraints:**

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

## Video Explanation

[Linkedin Interview Question - Reorder List - Leetcode 143 - Python](https://www.youtube.com/watch?v=S5bfdUTrKLM)

## Approach

### Intuition

The target order alternates the first half with the reversed second half.

### Brute Force

Store all node references in an array and reconnect them from the two ends inward.

### Optimal

Find the midpoint, reverse the second half in place, then weave nodes from both halves together.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- Lists with fewer than three nodes need no meaningful reorder.
- Terminate the first half before reversing so the original halves do not remain linked.
- The final node may be from either half; ensure no cycle remains.
