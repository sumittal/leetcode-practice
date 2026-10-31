# 72. Edit Distance

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/edit-distance/](https://leetcode.com/problems/edit-distance/)

## Problem

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

**Example 1:**

```

**Input:** word1 = "horse", word2 = "ros"
**Output:** 3
**Explanation:**
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

**Example 2:**

```

**Input:** word1 = "intention", word2 = "execution"
**Output:** 5
**Explanation:**
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

```

**Constraints:**

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Video Explanation

[Edit Distance - Dynamic Programming - Leetcode 72 - Python](https://www.youtube.com/watch?v=XYi2-LPrwm4)

## Approach

### Intuition

Transforming prefixes requires either a matching final character or one insert, delete, or replace operation.

### Brute Force

Recursively try all three edits at each pair of mismatching suffix characters.

### Optimal

Build prefix edit distances row by row, retaining only the previous row and current row.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(m+n) |
| Optimal | O(mn) | O(min(m,n)) |

### Edge cases

- Transforming an empty string requires one insertion per target character.
- Equal strings require zero edits.
