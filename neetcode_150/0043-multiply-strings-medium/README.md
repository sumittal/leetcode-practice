# 43. Multiply Strings

**Difficulty:** Medium  
**Tags:** Math, String, Simulation  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/multiply-strings/](https://leetcode.com/problems/multiply-strings/)

## Problem

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

```
**Input:** num1 = "2", num2 = "3"
**Output:** "6"

```

**Example 2:**

```
**Input:** num1 = "123", num2 = "456"
**Output:** "56088"

```

**Constraints:**

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Video Explanation

[Multiply Strings - Leetcode 43 - Python](https://www.youtube.com/watch?v=1vZswirL8Y8)

## Approach

### Intuition

Each digit product contributes to two neighboring positions in the decimal result array.

### Brute Force

Convert both strings to arbitrary-precision integers, multiply, and stringify.

### Optimal

Multiply digit pairs into a result array and propagate carries without converting either full input.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(mn) arithmetic for digit-length multiplication | O(m+n) |
| Optimal | O(mn) | O(m+n) |

### Edge cases

- If either input is zero, the product is the string zero.
- Leading zero positions in the result array must not appear in the returned string.
