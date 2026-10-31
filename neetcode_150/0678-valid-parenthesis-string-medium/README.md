# 678. Valid Parenthesis String

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Stack, Greedy, Bracket Sequences  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/valid-parenthesis-string/](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` *if* `s` *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

**Example 1:**

```

**Input:** s = "()"
**Output:** true

```

**Example 2:**

```

**Input:** s = "(*)"
**Output:** true

```

**Example 3:**

```

**Input:** s = "(*))"
**Output:** true

```

**Example 4:**

```

**Input:** s = "("
**Output:** false

```

**Constraints:**

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## Video Explanation

[Valid Parenthesis String - Leetcode 678 - Python](https://www.youtube.com/watch?v=QhPdNS143Qg)

## Approach

### Intuition

A star can be left as empty, treated as an opening parenthesis, or treated as a closing one.

### Brute Force

Recursively try all three interpretations of every star and check balance.

### Optimal

Track the minimum and maximum possible open-parenthesis counts after each prefix.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(3^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A prefix with no possible nonnegative balance is invalid.
- An empty string is balanced.
