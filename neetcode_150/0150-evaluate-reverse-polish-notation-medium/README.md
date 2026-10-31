# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium  
**Tags:** Array, Math, Stack  
**Companies:** Apollo.io, Citigroup, Canonical, Citadel, Grammarly, Anduril, Tesla, LinkedIn, Bloomberg, Amazon, tcs, Microsoft, Google, Yandex, Meta (+4 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/evaluate-reverse-polish-notation/](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Problem

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

**Example 1:**

```

**Input:** tokens = ["2","1","+","3","*"]
**Output:** 9
**Explanation:** ((2 + 1) * 3) = 9

```

**Example 2:**

```

**Input:** tokens = ["4","13","5","/","+"]
**Output:** 6
**Explanation:** (4 + (13 / 5)) = 6

```

**Example 3:**

```

**Input:** tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**Output:** 22
**Explanation:** ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

```

**Constraints:**

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## Video Explanation

[Evaluate Reverse Polish Notation - Leetcode 150 - Python](https://www.youtube.com/watch?v=iu0082c4HDE)

## Approach

### Intuition

In postfix notation, each operator combines the two most recently produced operands.

### Brute Force

Repeatedly locate an operator and replace it with the result of its preceding operands.

### Optimal

Use a stack; pop the right operand before the left operand for each operator.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- Division truncates toward zero rather than rounding down.
- Subtraction and division are not commutative, so operand order matters.
