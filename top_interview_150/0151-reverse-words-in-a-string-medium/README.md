# 151. Reverse Words in a String

**Difficulty:** Medium  
**Tags:** Two Pointers, String  
**Companies:** Yelp, Nykaa, Snap, Deutsche Bank, Apple, Zopsmart, Microsoft, ServiceNow, Nvidia, Infosys, Bloomberg, Barclays, Capgemini, Amazon, EPAM Systems (+10 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/reverse-words-in-a-string/](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**

```

**Input:** s = "the sky is blue"
**Output:** "blue is sky the"

```

**Example 2:**

```

**Input:** s = "  hello world  "
**Output:** "world hello"
**Explanation:** Your reversed string should not contain leading or trailing spaces.

```

**Example 3:**

```

**Input:** s = "a good   example"
**Output:** "example good a"
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

```

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is **at least one** word in `s`.

**Follow-up:** If the string data type is mutable in your language, can you solve it **in-place** with `O(1)` extra space?

## Video Explanation

[YouTube search: Search YouTube for leetcode 151 Reverse Words in a String neetcode](https://www.youtube.com/results?search_query=leetcode+151+Reverse+Words+in+a+String+neetcode)

## Approach

### Intuition

The requested result is the sequence of nonempty whitespace-delimited words in reverse order.

### Brute Force

Repeatedly find the last word and remove it from the remaining prefix.

### Optimal

Split on whitespace, reverse the resulting words, and join them with one space.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- Leading and trailing spaces disappear.
- Multiple spaces between words become one space.
- A single word remains unchanged.
