# 125. Valid Palindrome

**Difficulty:** Easy  
**Tags:** Two Pointers, String  
**Companies:** Zenefits, Cadence, Meta, Comcast, LTI, HCL, Pwc, Yandex, Apple, tcs, Altimetrik, VK, Fidelity, Axon, Cognizant (+24 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or* `false`* otherwise*.

**Example 1:**

```

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**

```

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

```

**Example 3:**

```

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

**Constraints:**

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Video Explanation

[Valid Palindrome - Leetcode 125 - Python](https://www.youtube.com/watch?v=jJXJ16kPFWg)

## Approach

### Intuition

A palindrome reads the same in both directions. Compare the next relevant character from each end while ignoring punctuation, spaces, and case.

### Brute Force

Build a normalized string containing only alphanumeric characters, then compare it with its reverse.

### Optimal

Move two pointers inward, skipping non-alphanumeric characters and comparing the case-folded characters in place.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A string with no alphanumeric characters is a palindrome.
- Skip punctuation and whitespace before comparing.
- Use case-insensitive comparisons.
