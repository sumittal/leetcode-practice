# 21. Merge Two Sorted Lists

**Difficulty:** Easy  
**Tags:** Linked List, Recursion  
**Companies:** Wix, Bloomberg, Qualcomm, Hubspot, Amazon, ServiceNow, Microsoft, Siemens, Docusign, Rippling, Squarespace, Yandex, Google, Capgemini, Apple (+17 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

```

**Example 2:**

```

**Input:** list1 = [], list2 = []
**Output:** []

```

**Example 3:**

```

**Input:** list1 = [], list2 = [0]
**Output:** [0]

```

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Video Explanation

[Merge Two Sorted Lists - Leetcode 21 - Python](https://www.youtube.com/watch?v=XIdigk956u0)

## Approach

### Intuition

The smallest remaining node must be one of the two list heads.

### Brute Force

Collect all values, sort them, and build a new linked list.

### Optimal

Use a sentinel and repeatedly attach the smaller current node, then append whichever list remains.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((m+n) log(m+n)) | O(m+n) |
| Optimal | O(m+n) | O(1) extra |

### Edge cases

- Either input list may be empty.
- Equal values can be taken from either list without changing sorted order.
- Append the untouched remainder once one list is exhausted.
