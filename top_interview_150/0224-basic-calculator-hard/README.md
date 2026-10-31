# 224. Basic Calculator

**Difficulty:** Hard  
**Tags:** Math, String, Stack, Recursion  
**Companies:** Rokt, Squarepoint Capital, Ripple, Snap, Uber, Snowflake, ByteDance, TikTok, Tesla, Microsoft, Amazon, Palo Alto Networks, Google, Meta, DoorDash (+7 more)  
**Pattern:** Math  
**LeetCode:** [https://leetcode.com/problems/basic-calculator/](https://leetcode.com/problems/basic-calculator/)

## Problem

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return *the result of the evaluation*.

**Note:** You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

**Example 1:**

```

**Input:** s = "1 + 1"
**Output:** 2

```

**Example 2:**

```

**Input:** s = " 2-1 + 2 "
**Output:** 3

```

**Example 3:**

```

**Input:** s = "(1+(4+5+2)-3)+(6+8)"
**Output:** 23

```

**Constraints:**

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is **not** used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Video Explanation

[YouTube search: Search YouTube for leetcode 224 Basic Calculator neetcode](https://www.youtube.com/results?search_query=leetcode+224+Basic+Calculator+neetcode)

## Approach

### Intuition

Parentheses create nested expressions, while a running sign lets each signed number contribute directly to the current result.

### Brute Force

Recursively parse every parenthesized substring and evaluate its operators.

### Optimal

Scan once, accumulate multi-digit numbers, and save the outer result and sign on a stack at each opening parenthesis.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- Whitespace may appear anywhere.
- A unary sign can precede a parenthesized expression.
- Nested parentheses restore the enclosing result and sign when closed.
