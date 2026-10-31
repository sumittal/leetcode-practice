# 707. Design Linked List

**Difficulty:** Medium  
**Tags:** Linked List, Design  
**Companies:** Google, Microsoft, Apple, Amazon, Bloomberg, Meta  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/design-linked-list/](https://leetcode.com/problems/design-linked-list/)

## Problem

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are **0-indexed**.

Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Get the value of the `index^th` node in the linked list. If the index is invalid, return `-1`.
- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Add a node of value `val` before the `index^th` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node **will not be inserted**.
- `void deleteAtIndex(int index)` Delete the `index^th` node in the linked list, if the index is valid.

**Example 1:**

```

**Input**
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
**Output**
[null, null, null, null, 2, null, 3]

**Explanation**
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

```

**Constraints:**

- `0 <= index, val <= 1000`
- Please do not use the built-in LinkedList library.
- At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex` and `deleteAtIndex`.

## Video Explanation

[Design Linked List - Leetcode 707 - Python](https://www.youtube.com/watch?v=Wf4QhpdVFQo)

## Approach

### Intuition

A dummy head makes insertion and deletion at index zero follow the same predecessor logic as other positions.

### Brute Force

Store values in a dynamic array and shift elements after indexed insertions and deletions.

### Optimal

Use a singly linked list and walk to the predecessor for indexed operations.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | get O(1), addAtHead O(n), addAtTail O(1), addAtIndex O(n), deleteAtIndex O(n) | O(n) |
| Optimal | get O(n), addAtHead O(1), addAtTail O(n), addAtIndex O(n), deleteAtIndex O(n) | O(n) |

### Edge cases

- Invalid get indices return -1.
- An insertion at the current length appends, while larger indices are ignored.
