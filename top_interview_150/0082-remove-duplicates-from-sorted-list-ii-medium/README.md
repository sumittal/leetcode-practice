# 82. Remove Duplicates from Sorted List II

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers  
**Companies:** Arista Networks, Bloomberg, Google, Oracle, TikTok, Microsoft, Amazon, Apple, Meta  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem

You are given the `head` of a **sorted** linked list.

Delete all nodes that have **duplicate** numbers, leaving only **distinct** numbers from the original list.

Return the linked list **sorted** as well.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)

```

**Input:** head = [1,2,3,3,4,4,5]
**Output:** [1,2,5]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)

```

**Input:** head = [1,1,1,2,3]
**Output:** [2,3]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## Video Explanation

[YouTube search: Search YouTube for leetcode 82 Remove Duplicates from Sorted List II neetcode](https://www.youtube.com/results?search_query=leetcode+82+Remove+Duplicates+from+Sorted+List+II+neetcode)

## Approach

### Intuition

Because duplicates are adjacent in a sorted list, each run can be skipped entirely when its value occurs more than once.

### Brute Force

Copy all node values into a list, count them, then rebuild nodes for values occurring once.

### Optimal

Use a dummy predecessor and unlink each entire repeated-value run in one scan.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The head itself may be duplicated and removed.
- All nodes may belong to duplicate runs.
- An empty or singleton list is already duplicate-free.
