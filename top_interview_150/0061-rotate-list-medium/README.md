# 61. Rotate List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers  
**Companies:** Airwallex, Nvidia, josh technology, Bloomberg, Amazon, LinkedIn, Google, Oracle, Microsoft, Meta  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/rotate-list/](https://leetcode.com/problems/rotate-list/)

## Problem

Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

```

**Input:** head = [1,2,3,4,5], k = 2
**Output:** [4,5,1,2,3]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

```

**Input:** head = [0,1,2], k = 4
**Output:** [2,0,1]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Video Explanation

[Rotate List - Linked List - Leetcode 61 - Python](https://www.youtube.com/watch?v=UcGtPs2LE_c)

## Approach

### Intuition

A right rotation moves the final k nodes to the front, which can be done by temporarily making the list circular.

### Brute Force

Move the tail to the head one step at a time k times.

### Optimal

Find the length and tail, link tail to head, then break the ring at the new tail after reducing k modulo length.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nk) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- An empty or one-node list is unchanged.
- A rotation by a multiple of list length changes nothing.
- The new tail is length-k nodes from the original tail.
