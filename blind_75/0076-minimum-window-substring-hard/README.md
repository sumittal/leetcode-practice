# 76. Minimum Window Substring

**Difficulty:** Hard  
**Tags:** Hash Table, String, Sliding Window  
**Companies:** Wissen Technology, Lyft, Snowflake, Snap, Harness, DP world, SoFi, Moloco, Adobe, Zeta, Meta, TikTok, Qualtrics, LinkedIn, Amazon (+17 more)  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of* `s`* such that every character in* `t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string* `""`.

The testcases will be generated such that the answer is **unique**.

**Example 1:**

```

**Input:** s = "ADOBECODEBANC", t = "ABC"
**Output:** "BANC"
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

**Example 2:**

```

**Input:** s = "a", t = "a"
**Output:** "a"
**Explanation:** The entire string s is the minimum window.

```

**Example 3:**

```

**Input:** s = "a", t = "aa"
**Output:** ""
**Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

## Video Explanation

[Minimum Window Substring - Airbnb Interview Question - Leetcode 76](https://www.youtube.com/watch?v=jSto0O4AJbM)

## Approach

### Intuition

Expand a window until it contains all required character counts, then shrink its left edge while it remains valid.

### Brute Force

Enumerate substrings, count their characters, and keep the shortest substring covering every required count.

### Optimal

Track required and current counts plus how many distinct requirements are satisfied. Expand right, then contract left while all requirements remain satisfied.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((m+n) * m) | O(k) |
| Optimal | O(m+n) | O(k) |

### Edge cases

- An empty target needs no characters, so return the empty string.
- If the source is shorter than the target or lacks a required multiplicity, no window exists.
- Repeated characters in the target require matching counts, not just presence.
