# 763. Partition Labels

**Difficulty:** Medium  
**Tags:** Hash Table, Two Pointers, String, Greedy  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/partition-labels/](https://leetcode.com/problems/partition-labels/)

## Problem

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

**Example 1:**

```

**Input:** s = "ababcbacadefegdehijhklij"
**Output:** [9,7,8]
**Explanation:**
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

**Example 2:**

```

**Input:** s = "eccbbbbdec"
**Output:** [10]

```

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Video Explanation

[Partition Labels - Leetcode 763 - Python](https://www.youtube.com/watch?v=B7m8UmZE-vw)

## Approach

### Intuition

A partition can end only after the final occurrence of every character seen so far.

### Brute Force

Try every cut and verify that no character appears on both sides.

### Optimal

Precompute each character's last index and close a partition when the scan reaches the current farthest last occurrence.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) for a fixed alphabet |
| Optimal | O(n) | O(1) for a fixed alphabet |

### Edge cases

- A character occurring only once can form a one-character partition.
- If every character repeats across the string, the result may be one partition.
