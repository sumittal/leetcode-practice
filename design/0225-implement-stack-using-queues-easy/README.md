# 225. Implement Stack using Queues

**Difficulty:** Easy  
**Tags:** Stack, Design, Queue  
**Companies:** Nagarro, Qualcomm, Bloomberg, Google, Microsoft, Amazon, Meta, Goldman Sachs, Apple  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/implement-stack-using-queues/](https://leetcode.com/problems/implement-stack-using-queues/)

## Problem

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

**Example 1:**

```

**Input**
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
**Output**
[null, null, null, 2, 2, false]

**Explanation**
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

```

**Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

**Follow-up:** Can you implement the stack using only one queue?

## Video Explanation

[Implement Stack using Queues - Leetcode 225 - Python](https://www.youtube.com/watch?v=rW4vm0-DLYc)

## Approach

### Intuition

A queue exposes its oldest item, so rotating all older items behind a newly pushed value makes that value the front.

### Brute Force

Keep a list and remove its final element for each pop.

### Optimal

Use one queue and rotate the existing elements after each push so the newest value is at the front.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | push O(1), pop O(1), top O(1), empty O(1) | O(n) |
| Optimal | push O(n), pop O(1), top O(1), empty O(1) | O(n) |

### Edge cases

- The latest pushed value is always the next value removed.
- A one-element stack needs no rotation.
