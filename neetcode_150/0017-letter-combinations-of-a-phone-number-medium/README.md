# 17. Letter Combinations of a Phone Number

**Difficulty:** Medium  
**Tags:** Hash Table, String, Backtracking  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/letter-combinations-of-a-phone-number/](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

**Example 1:**

```

**Input:** digits = "23"
**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

**Example 2:**

```

**Input:** digits = "2"
**Output:** ["a","b","c"]

```

**Constraints:**

- `1 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Video Explanation

[Letter Combinations of a Phone Number - Backtracking - Leetcode 17](https://www.youtube.com/watch?v=0snEunUacZY)

## Approach

### Intuition

Each digit contributes one letter choice, so combinations are the Cartesian product of its mapped letters.

### Brute Force

Build every possible prefix combination iteratively for each digit.

### Optimal

Backtrack over the mapped letters for each digit and emit a string when all digits are consumed.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(4^n) | O(4^n) |
| Optimal | O(4^n) | O(n) besides output |

### Edge cases

- An empty digit string returns an empty result.
- Digits 7 and 9 each map to four letters.
