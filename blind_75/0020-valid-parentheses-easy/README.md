# 20. Valid Parentheses

**Difficulty:** Easy  
**Tags:** String, Stack, Bracket Sequences  
**Companies:** Intuit, Zenefits, FreshWorks, Chewy, Tripadvisor, Odoo, Walmart Labs, X, Bank of America, Zoho, HP, BlackRock, USAA, Intel, Siemens (+75 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Video Explanation

[Valid Parentheses - Stack - Leetcode 20 - Python](https://www.youtube.com/watch?v=WTzjTskDFMg)

## Approach

### Intuition

Every closing bracket must match the most recent unmatched opening bracket.

### Brute Force

Repeatedly remove adjacent matching bracket pairs until no more pairs can be removed.

### Optimal

Push opening brackets onto a stack; each closing bracket must match and pop the stack top.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty string is valid.
- A closing bracket with an empty stack is immediately invalid.
- A nonempty stack at the end means one or more openings were unmatched.
