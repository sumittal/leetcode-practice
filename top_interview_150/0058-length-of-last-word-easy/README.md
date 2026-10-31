# 58. Length of Last Word

**Difficulty:** Easy  
**Tags:** String  
**Companies:** tcs, Bloomberg, Google, Amazon, Microsoft, Meta  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/length-of-last-word/](https://leetcode.com/problems/length-of-last-word/)

## Problem

Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```

**Input:** s = "Hello World"
**Output:** 5
**Explanation:** The last word is "World" with length 5.

```

**Example 2:**

```

**Input:** s = "   fly me   to   the moon  "
**Output:** 4
**Explanation:** The last word is "moon" with length 4.

```

**Example 3:**

```

**Input:** s = "luffy is still joyboy"
**Output:** 6
**Explanation:** The last word is "joyboy" with length 6.

```

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Video Explanation

[Length of Last Word - Leetcode 58 - Python](https://www.youtube.com/watch?v=KT9rltZTybQ)

## Approach

### Intuition

After trimming trailing spaces, the last word is the final contiguous run of non-space characters.

### Brute Force

Split the string on whitespace and return the length of the final token.

### Optimal

Scan backward over trailing spaces, then count characters until the preceding space or beginning.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The input may have leading or trailing spaces.
- The string contains at least one word.
- A one-word string returns its full length.
