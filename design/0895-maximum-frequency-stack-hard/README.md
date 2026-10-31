# 895. Maximum Frequency Stack

**Difficulty:** Hard  
**Tags:** Hash Table, Stack, Design, Ordered Set  
**Companies:** Nutanix, Salesforce, Expedia, Flipkart, Apple, Amazon, Uber, Microsoft, Bloomberg, Meta, Google  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/maximum-frequency-stack/](https://leetcode.com/problems/maximum-frequency-stack/)

## Problem

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:

- `FreqStack()` constructs an empty frequency stack.
- `void push(int val)` pushes an integer `val` onto the top of the stack.
- `int pop()` removes and returns the most frequent element in the stack.
  - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

**Example 1:**

```

**Input**
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
**Output**
[null, null, null, null, null, null, null, 5, 7, 5, 4]

**Explanation**
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

```

**Constraints:**

- `0 <= val <= 10^9`
- At most `2 * 10^4` calls will be made to `push` and `pop`.
- It is guaranteed that there will be at least one element in the stack before calling `pop`.

## Video Explanation

[Maximum Frequency Stack - Leetcode 895 - Python](https://www.youtube.com/watch?v=Z6idIicFDOE)

## Approach

### Intuition

The most frequent value wins, with the most recently pushed value breaking ties.

### Brute Force

Count all values and scan the complete push history to find the most frequent latest value on every pop.

### Optimal

Track each value's frequency and keep a stack of values for each frequency level.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | push O(1), pop O(n) | O(n) |
| Optimal | push O(1), pop O(1) | O(n) |

### Edge cases

- When frequencies tie, the latest value in that frequency stack is removed.
- The maximum frequency decreases when its final value is popped.
