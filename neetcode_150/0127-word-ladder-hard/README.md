# 127. Word Ladder

**Difficulty:** Hard  
**Tags:** Hash Table, String, Breadth-First Search, Bidirectional Search  
**Companies:** Navan, Yelp, Snap, Reddit, The Trade Desk, LinkedIn, Box, Okta, Amazon, ByteDance, Apple, Citadel, Docusign, eBay, Tekion (+19 more)  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/word-ladder/](https://leetcode.com/problems/word-ladder/)

## Problem

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub>` such that:

- Every adjacent pair of words differs by a single letter.
- Every `s<sub>i</sub>` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `s<sub>k</sub> == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *the **number of words** in the **shortest transformation sequence** from* `beginWord` *to* `endWord`*, or* `0`* if no such sequence exists.*

**Example 1:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** 5
**Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

```

**Example 2:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** 0
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

```

**Constraints:**

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are **unique**.

## Video Explanation

[Word Ladder - Breadth First Search - Leetcode 127 - Python](https://www.youtube.com/watch?v=h9iTnkgv05E)

## Approach

### Intuition

A shortest transformation uses one-letter changes, so breadth-first search explores words in increasing path length.

### Brute Force

Compare every discovered word against every dictionary word to find one-letter neighbors.

### Optimal

Build wildcard-pattern buckets and use BFS to visit each transformation level.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(N^2 L) | O(N) |
| Optimal | O(N L^2) | O(N L) |

### Edge cases

- If the end word is absent from the dictionary, no sequence can reach it.
- The sequence length includes both the begin and end words.
