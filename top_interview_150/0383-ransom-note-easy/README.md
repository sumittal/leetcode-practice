# 383. Ransom Note

**Difficulty:** Easy  
**Tags:** Hash Table, String, Counting  
**Companies:** Criteo, Karat, Tripadvisor, Spotify, SAP, Anduril, Apple, Microsoft, Google, Amazon, Bloomberg, Meta, tcs  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/ransom-note/](https://leetcode.com/problems/ransom-note/)

## Problem

Given two strings `ransomNote` and `magazine`, return `true`* if* `ransomNote`* can be constructed by using the letters from* `magazine`* and* `false`* otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**

```
**Input:** ransomNote = "a", magazine = "b"
**Output:** false

```

**Example 2:**

```
**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false

```

**Example 3:**

```
**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true

```

**Constraints:**

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Video Explanation

[YouTube search: Search YouTube for leetcode 383 Ransom Note neetcode](https://www.youtube.com/results?search_query=leetcode+383+Ransom+Note+neetcode)

## Approach

### Intuition

Each magazine character can be used once, so the magazine must contain every ransom-note character at least as often.

### Brute Force

For each note character, search for and remove one matching magazine character.

### Optimal

Count magazine characters and decrement the required count for each note character.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nm) | O(m) |
| Optimal | O(n+m) | O(Σ) |

### Edge cases

- An empty ransom note can always be constructed.
- Repeated note letters require repeated magazine letters.
- The note cannot use any character more often than the magazine provides.
