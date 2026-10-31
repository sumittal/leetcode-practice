# 13. Roman to Integer

**Difficulty:** Easy  
**Tags:** Hash Table, Math, String  
**Companies:** AMD, Yahoo, IBM, Warnermedia, Virtusa, Tinkoff, Pwc, tcs, Bloomberg, Microsoft, Cashfree, Google, Meta, Amazon, EPAM Systems (+19 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

## Problem

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```

**Symbol**       **Value**
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```

**Input:** s = "III"
**Output:** 3
**Explanation:** III = 3.

```

**Example 2:**

```

**Input:** s = "LVIII"
**Output:** 58
**Explanation:** L = 50, V= 5, III = 3.

```

**Example 3:**

```

**Input:** s = "MCMXCIV"
**Output:** 1994
**Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.

```

**Constraints:**

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Video Explanation

[Roman to Integer - Leetcode 13 - Python](https://www.youtube.com/watch?v=3jdxYj3DD98)

## Approach

### Intuition

A Roman numeral symbol subtracts when it is smaller than the symbol immediately to its right; otherwise it adds.

### Brute Force

Parse each allowed two-symbol subtractive pair separately, then sum remaining symbols.

### Optimal

Scan symbols once, adding or subtracting each value based on its next symbol.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- A one-symbol numeral is its direct value.
- Subtractive pairs include IV, IX, XL, XC, CD, and CM.
- The final symbol is always added.
