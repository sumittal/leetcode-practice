# 97. Interleaving String

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/interleaving-string/](https://leetcode.com/problems/interleaving-string/)

## Problem

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- `s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub>`
- `t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub>`
- `|n - m| <= 1`
- The **interleaving** is `s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...` or `t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...`

**Note:** `a + b` is the concatenation of strings `a` and `b`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

```

**Input:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
**Output:** true
**Explanation:** One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

```

**Example 2:**

```

**Input:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
**Output:** false
**Explanation:** Notice how it is impossible to interleave s2 with any other string to obtain s3.

```

**Example 3:**

```

**Input:** s1 = "", s2 = "", s3 = ""
**Output:** true

```

**Constraints:**

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters.

**Follow up:** Could you solve it using only `O(s2.length)` additional memory space?

## Video Explanation

[Interleaving Strings - Dynamic Programming - Leetcode 97 - Python](https://www.youtube.com/watch?v=3Rw3p9LrgvE)

## Approach

### Intuition

A prefix of the result is valid if its last character can come from either source string after a valid earlier prefix.

### Brute Force

Recursively try matching the next result character against either source string.

### Optimal

Use a rolling one-dimensional DP over the second string, updating each state from the prior row or current row's left neighbor.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^(m+n)) | O(m+n) |
| Optimal | O(mn) | O(n) |

### Edge cases

- The combined lengths must equal the result length.
- Either source string may be empty.
