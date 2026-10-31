# 716. Max Stack

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Linked List, Stack, Design, Doubly-Linked List, Ordered Set  
**Companies:** LinkedIn, Roku, Walmart Labs, Nutanix, Lyft, TikTok, Amazon, Meta, Google  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/max-stack/](https://leetcode.com/problems/max-stack/)

## Problem

Create a stack that supports ordinary push, pop, and top operations as well as reading or removing its maximum value. When several entries share the maximum, popMax removes the one nearest the stack top. Example 1: push 5, 1, 5; top and popMax both return 5; the remaining top is 1 and the maximum is still 5. Example 2: push -2, -2, then popMax removes one -2 while the other remains. Constraints: the stack is nonempty whenever a removal or read is requested.

## Video Explanation

[YouTube search: Search YouTube for leetcode 716 Max Stack neetcode](https://www.youtube.com/results?search_query=leetcode+716+Max+Stack+neetcode)

## Approach

### Intuition

A list preserves stack order and lets a scan find the most recent occurrence of the maximum.

### Brute Force

Store values in a list, scanning it for the maximum and deleting that occurrence when requested.

### Optimal

Maintain a doubly linked list for stack order and an ordered structure for maximum values.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | push O(1), pop O(1), top O(1), peekMax O(n), popMax O(n) | O(n) |
| Optimal | push O(log n), pop O(log n), top O(1), peekMax O(1), popMax O(log n) | O(n) |

### Edge cases

- When maximum values tie, remove the newest such entry.
- Negative values are valid stack entries.
