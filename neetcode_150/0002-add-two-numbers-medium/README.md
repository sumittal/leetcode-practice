# 2. Add Two Numbers

**Difficulty:** Medium  
**Tags:** Linked List, Math, Recursion  
**Companies:** EarnIn, Adobe, Wix, Bloomberg, Microsoft, LTI, Amazon, Google, Meta, Jane Street, Airbnb, AQR Capital Management, Zoho, SAP, Arista Networks (+18 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

## Problem

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

```

**Example 2:**

```

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

```

**Example 3:**

```

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

```

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Video Explanation

[Add Two Numbers - Leetcode 2 - Python](https://www.youtube.com/watch?v=wgFPrzTjm7s)

## Approach

### Intuition

The lists store digits least-significant first, so ordinary addition proceeds from their heads with a carry.

### Brute Force

Convert both lists to integers, add them, and convert the result back into a list.

### Optimal

Add corresponding digits in one pass, keeping a carry and appending each result digit.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n+m) | O(n+m) |
| Optimal | O(max(n,m)) | O(max(n,m)) for the result |

### Edge cases

- The final addition may produce an extra carry node.
- The two lists may have different lengths.
