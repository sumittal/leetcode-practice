# 148. Sort List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort  
**Companies:** Lyft, ByteDance, Amazon, Google, Bloomberg, Microsoft, Meta, Oracle, TikTok  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/sort-list/](https://leetcode.com/problems/sort-list/)

## Problem

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

```

**Input:** head = [4,2,1,3]
**Output:** [1,2,3,4]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

```

**Input:** head = [-1,5,3,4,0]
**Output:** [-1,0,3,4,5]

```

**Example 3:**

```

**Input:** head = []
**Output:** []

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

## Video Explanation

[Sort List - Merge Sort - Leetcode 148](https://www.youtube.com/watch?v=TGveA1oFhrc)

## Approach

### Intuition

Split the linked list into halves, sort each half, then merge the sorted chains.

### Brute Force

Copy node values into an array, sort them, and write them back into the list.

### Optimal

Use top-down merge sort with slow-fast midpoint splitting and an in-place linked-list merge.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(n log n) | O(log n) recursion |

### Edge cases

- An empty or one-node list is already sorted.
- Duplicate and negative values retain correct sorted order.
- The returned list reuses the original nodes.
