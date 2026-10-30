# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Tags:** Hash Table, String, Sliding Window  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**Example 1:**

```

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

**Example 2:**

```

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

```

**Example 3:**

```

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

**Constraints:**

- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols and spaces.

## Video Explanation

[Longest Substring Without Repeating Characters - Leetcode 3 - Python](https://www.youtube.com/watch?v=wiGpQwVHdE0)

## Approach

### Intuition

Maintain a window with unique characters; when a repeated character appears, move the left edge past its previous occurrence.

### Brute Force

Check every substring and test whether its characters are unique.

### Optimal

Track each character's most recent index and move the left boundary forward only when that occurrence is inside the current window.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^3) | O(k) |
| Optimal | O(n) | O(k) |

### Edge cases

- An empty string has answer zero.
- Repeated adjacent characters reduce the window to one character.
- A previous occurrence before the current window must not move the left boundary backward.
