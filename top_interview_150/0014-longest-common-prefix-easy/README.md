# 14. Longest Common Prefix

**Difficulty:** Easy  
**Tags:** Array, String, Trie  
**Companies:** Revolut, USAA, CME Group, Yelp, Target, Disney, oyo, Nokia, Sigmoid, Wipro, opentext, Pwc, HSBC, SAP, Bloomberg (+37 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

```

**Example 2:**

```

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Video Explanation

[Longest Common Prefix - Leetcode 14 - Python](https://www.youtube.com/watch?v=0sWShKIJoo4)

## Approach

### Intuition

A common prefix cannot extend beyond the shortest input or the first position that disagrees.

### Brute Force

Compare every character position in all strings until one string ends or a mismatch appears.

### Optimal

Shrink a candidate prefix against each string until that string starts with it.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nm) | O(1) |
| Optimal | O(nm) | O(1) |

### Edge cases

- An empty list has no prefix.
- An empty string forces an empty common prefix.
- A single string is its own longest prefix.
