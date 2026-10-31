# 115. Distinct Subsequences

**Difficulty:** Hard  
**Tags:** String, Dynamic Programming  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/distinct-subsequences/](https://leetcode.com/problems/distinct-subsequences/)

## Problem

Given two strings s and t, return *the number of distinct* ***subsequences**** of* s* which equals* t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

**Example 1:**

```

**Input:** s = "rabbbit", t = "rabbit"
**Output:** 3
**Explanation:**
As shown below, there are 3 ways you can generate "rabbit" from s.
**rabb**b**it**
**ra**b**bbit**
**rab**b**bit**

```

**Example 2:**

```

**Input:** s = "babgbag", t = "bag"
**Output:** 5
**Explanation:**
As shown below, there are 5 ways you can generate "bag" from s.
**ba**b**g**bag
**ba**bgba**g**
**b**abgb**ag**
ba**b**gb**ag**
babg**bag**
```

**Constraints:**

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Video Explanation

[Distinct Subsequences - Dynamic Programming - Leetcode 115 - Python](https://www.youtube.com/watch?v=-RDzMJ33nx8)

## Approach

### Intuition

Each source character can be skipped, or matched to the next needed target character.

### Brute Force

Recursively choose whether each source position participates in a matching subsequence.

### Optimal

Count ways for each target prefix in one dimension, scanning target positions backward so a source character is used once.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^m) | O(m+n) |
| Optimal | O(mn) | O(n) |

### Edge cases

- The empty target has one matching subsequence.
- A target longer than the source has zero matches.
