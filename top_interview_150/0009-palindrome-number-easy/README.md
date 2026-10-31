# 9. Palindrome Number

**Difficulty:** Easy  
**Tags:** Math  
**Companies:** Bosch, Cognizant, tcs, PornHub, Accenture, SAP, LTI, Qualcomm, Google, Infosys, Microsoft, Wipro, Bloomberg, Morgan Stanley, MindTree (+15 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

## Problem

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

**Example 1:**

```

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

```

**Example 2:**

```

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

**Example 3:**

```

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

```

**Constraints:**

- `-2^31 <= x <= 2^31 - 1`

**Follow up:** Could you solve it without converting the integer to a string?

## Video Explanation

[Palindrome Number - Leetcode 9 - Python](https://www.youtube.com/watch?v=yubRKwixN-U)

## Approach

### Intuition

A nonnegative number is palindromic when its leading and trailing digits mirror each other.

### Brute Force

Convert the number to text and compare it with its reversal.

### Optimal

Reverse only the lower half of the digits and compare the halves.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(d) | O(d) |
| Optimal | O(d) | O(1) |

### Edge cases

- Negative numbers are not palindromes.
- A nonzero number ending in zero cannot be a palindrome.
- Odd-length numbers ignore the middle digit when comparing halves.
