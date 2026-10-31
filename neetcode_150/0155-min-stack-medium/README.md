# 155. Min Stack

**Difficulty:** Medium  
**Tags:** Stack, Design  
**Companies:** Paytm, Zenefits, Odoo, Sigmoid, Snap, Tinkoff, Bloomberg, Vimeo, Ozon, Lucid, AMD, Intel, UiPath, Tripadvisor, Lyft (+21 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/)

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int value)` pushes the element `value` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

```

**Input**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**Output**
[null,null,null,null,-3,null,0,-2]

**Explanation**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

```

**Constraints:**

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Video Explanation

[Design Min Stack - Amazon Interview Question - Leetcode 155 - Python](https://www.youtube.com/watch?v=qkLl7nAwDPo)

## Approach

### Intuition

Store each value together with the minimum up through that stack position.

### Brute Force

Keep a normal stack and scan all values whenever getMin is called.

### Optimal

Keep a parallel minimum stack so every operation, including getMin, is constant time.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) for getMin; O(1) for other operations | O(n) |
| Optimal | O(1) per operation | O(n) |

### Edge cases

- Duplicate minimum values remain minimum after one copy is popped.
- The operation sequence may repeatedly push and pop values.
