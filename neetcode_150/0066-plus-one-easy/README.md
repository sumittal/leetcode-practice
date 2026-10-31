# 66. Plus One

**Difficulty:** Easy  
**Tags:** Array, Math  
**Companies:** Intuit, Bloomberg, Google, Meta, Zoho, Capgemini, tcs, Amazon, Microsoft, Visa  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/plus-one/](https://leetcode.com/problems/plus-one/)

## Problem

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

**Example 1:**

```

**Input:** digits = [1,2,3]
**Output:** [1,2,4]
**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

```

**Example 2:**

```

**Input:** digits = [4,3,2,1]
**Output:** [4,3,2,2]
**Explanation:** The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

```

**Example 3:**

```

**Input:** digits = [9]
**Output:** [1,0]
**Explanation:** The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

```

**Constraints:**

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s.

## Video Explanation

[Plus One - Leetcode 66 - Python](https://www.youtube.com/watch?v=jIaA8boiG1s)

## Approach

### Intuition

Only a suffix of nines changes; the first earlier non-nine digit absorbs the carry.

### Brute Force

Convert all digits to an integer, add one, and convert back to digits.

### Optimal

Walk backward, zeroing nines until a digit can be incremented; prepend one if carry remains.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) extra apart from output |

### Edge cases

- A non-nine final digit increments directly.
- An all-nine number grows by one digit.
