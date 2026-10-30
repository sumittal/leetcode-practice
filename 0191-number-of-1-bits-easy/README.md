# 191. Number of 1 Bits

**Difficulty:** Easy  
**Tags:** Divide and Conquer, Bit Manipulation  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/number-of-1-bits/](https://leetcode.com/problems/number-of-1-bits/)

## Problem

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

**Example 1:**

**Input:** n = 11

**Output:** 3

**Explanation:**

The input binary string **1011** has a total of three set bits.

**Example 2:**

**Input:** n = 128

**Output:** 1

**Explanation:**

The input binary string **10000000** has a total of one set bit.

**Example 3:**

**Input:** n = 2147483645

**Output:** 30

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total of thirty set bits.

**Constraints:**

- `1 <= n <= 2^31 - 1`

**Follow up:** If this function is called many times, how would you optimize it?

## Video Explanation

[Number of 1 Bits - Leetcode 191 - Python](https://www.youtube.com/watch?v=5Km3utixwZs)

## Approach

### Intuition

Each set bit can be removed by clearing the lowest set bit.

### Brute Force

Convert to binary text and count the ones.

### Optimal

Repeatedly apply n &= n-1 until no set bits remain.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(w) | O(w) |
| Optimal | O(number of set bits) | O(1) |

### Edge cases

- Zero has no set bits.
- Input is treated as a fixed-width unsigned bit pattern.
