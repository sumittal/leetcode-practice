# 67. Add Binary

**Difficulty:** Easy  
**Tags:** Math, String, Bit Manipulation, Simulation  
**Companies:** Wipro, Deloitte, Google, Bloomberg, Meta, Capgemini, tcs, Amazon, Microsoft, Snap, Walmart Labs, Zoho, Visa, IBM, Infosys (+1 more)  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/add-binary/](https://leetcode.com/problems/add-binary/)

## Problem

Given two binary strings `a` and `b`, return *their sum as a binary string*.

**Example 1:**

```
**Input:** a = "11", b = "1"
**Output:** "100"

```

**Example 2:**

```
**Input:** a = "1010", b = "1011"
**Output:** "10101"

```

**Constraints:**

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Video Explanation

[Add Binary - Leetcode 67 - Python](https://www.youtube.com/watch?v=keuWJ47xG8g)

## Approach

### Intuition

Add corresponding bits from right to left while carrying overflow to the next position.

### Brute Force

Parse both strings as integers, add them, and convert the result back to binary.

### Optimal

Use two indices and a carry, appending each output bit before reversing once.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- Adding zero to a binary number preserves its value.
- A carry can extend the output by one leading bit.
- Inputs may have different lengths.
