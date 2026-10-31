# 424. Longest Repeating Character Replacement

**Difficulty:** Medium  
**Tags:** Hash Table, String, Sliding Window  
**Companies:** Pocket Gems, CRED, ServiceNow, Publicis Sapient, UiPath, Bloomberg, InMobi, Amazon, DE Shaw, Microsoft, Infosys, Google, Zoho, ByteDance, Meta (+3 more)  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

**Example 1:**

```

**Input:** s = "ABAB", k = 2
**Output:** 4
**Explanation:** Replace the two 'A's with two 'B's or vice versa.

```

**Example 2:**

```

**Input:** s = "AABABBA", k = 1
**Output:** 4
**Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Video Explanation

[Longest Repeating Character Replacement - Leetcode 424 - Python](https://www.youtube.com/watch?v=gqXU1UyA8pk)

## Approach

### Intuition

A window can be made uniform when its length minus its most frequent character count is at most k.

### Brute Force

Enumerate substrings, count their characters, and check the minimum number of replacements needed.

### Optimal

Use a sliding window with character counts and a running maximum frequency; shrink when the window needs more than k replacements.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- With k equal to zero, only an existing repeated-character run can be used.
- An empty string yields zero.
- The running maximum frequency may be stale after shrinking; retaining it avoids rescans and still preserves the maximum window length.
