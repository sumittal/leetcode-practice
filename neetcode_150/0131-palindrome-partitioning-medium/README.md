# 131. Palindrome Partitioning

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Backtracking  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/palindrome-partitioning/](https://leetcode.com/problems/palindrome-partitioning/)

## Problem

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of* `s`.

**Example 1:**

```
**Input:** s = "aab"
**Output:** [["a","a","b"],["aa","b"]]

```

**Example 2:**

```
**Input:** s = "a"
**Output:** [["a"]]

```

**Constraints:**

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Video Explanation

[Palindrome Partitioning - Backtracking - Leetcode 131](https://www.youtube.com/watch?v=3jvWodd7ht0)

## Approach

### Intuition

Choose each possible palindromic prefix, then partition the remaining suffix recursively.

### Brute Force

Enumerate every cut pattern and test every resulting substring for palindromicity.

### Optimal

Backtrack over end indices and recurse only when the chosen substring is a palindrome.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n 2^n) | O(n) besides output |
| Optimal | O(n 2^n) | O(n) besides output |

### Edge cases

- An empty string has one partition containing no substrings.
- A string of identical characters has a partition at every possible set of cuts.
