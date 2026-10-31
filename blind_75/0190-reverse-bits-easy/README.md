# 190. Reverse Bits

**Difficulty:** Easy  
**Tags:** Divide and Conquer, Bit Manipulation  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/reverse-bits/](https://leetcode.com/problems/reverse-bits/)

## Problem

Reverse bits of a given 32 bits signed integer.

**Example 1:**

**Input:** n = 43261596

**Output:** 964176192

**Explanation:**

Integer Binary   43261596 00000010100101000001111010011100   964176192 00111001011110000010100101000000

**Example 2:**

**Input:** n = 2147483644

**Output:** 1073741822

**Explanation:**

Integer Binary   2147483644 01111111111111111111111111111100   1073741822 00111111111111111111111111111110

**Constraints:**

- `0 <= n <= 2^31 - 2`
- `n` is even.

**Follow up:** If this function is called many times, how would you optimize it?

## Video Explanation

[Reverse Bits - Binary - Leetcode 190 - Python](https://www.youtube.com/watch?v=UcoN6UjAI64)

## Approach

### Intuition

Build the result from low to high bits while shifting each source bit into its mirrored position.

### Brute Force

Format as a 32-character binary string, reverse it, and parse it.

### Optimal

Repeat 32 times: shift result left, append n's low bit, then shift n right.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(32) | O(32) |
| Optimal | O(1) | O(1) |

### Edge cases

- Always process exactly 32 bits, including leading zeroes.
- Python integers do not have a fixed width, so mask input bits as needed.
