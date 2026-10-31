# 139. Word Break

**Difficulty:** Medium  
**Tags:** Array, Hash Table, String, Dynamic Programming, Trie, Memoization, Brute-Force Search  
**Companies:** Pocket Gems, Coupang, Yahoo, MongoDB, Walmart Labs, Millennium, Compass, Intuit, Grammarly, Zeta, Uber, Arista Networks, Nutanix, Autodesk, Amazon (+11 more)  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)

## Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

```

**Input:** s = "leetcode", wordDict = ["leet","code"]
**Output:** true
**Explanation:** Return true because "leetcode" can be segmented as "leet code".

```

**Example 2:**

```

**Input:** s = "applepenapple", wordDict = ["apple","pen"]
**Output:** true
**Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

```

**Example 3:**

```

**Input:** s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
**Output:** false

```

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

## Video Explanation

[Word Break - Dynamic Programming - Leetcode 139 - Python](https://www.youtube.com/watch?v=Sx9NNgInc3A)

## Approach

### Intuition

A prefix is segmentable if some dictionary word ends there after a segmentable prefix.

### Brute Force

Try every word sequence recursively from each index.

### Optimal

DP over prefix endpoints, checking dictionary words that can end at each reachable position.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(n) |
| Optimal | O(n^2) | O(n) |

### Edge cases

- An empty prefix is reachable.
- A matching suffix alone is insufficient if the preceding prefix cannot be segmented.
