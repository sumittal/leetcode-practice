# 1804. Implement Trie II (Prefix Tree)

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, String, Design, Trie  
**Companies:** Amazon  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/implement-trie-ii-prefix-tree/](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)

## Problem

Implement a trie that supports insertion, exact-word counts, prefix counts, and erasing one copy of an inserted word. Example 1: after inserting apple, search counts apple once, app zero times, and the app prefix once; after inserting app and erasing it, app's exact count is zero. Example 2: inserting the same word twice and erasing it once leaves one copy. Constraints: words contain lowercase English letters and erase is called for a word present in the trie.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1804 Implement Trie II (Prefix Tree) neetcode](https://www.youtube.com/results?search_query=leetcode+1804+Implement+Trie+II+%28Prefix+Tree%29+neetcode)

## Approach

### Intuition

Trie nodes share common prefixes, while counters distinguish how many inserted words pass through or end at each node.

### Brute Force

Store every word in a list and scan the list for exact and prefix counts.

### Optimal

Store child links, a pass count, and an ending count at each trie node.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | insert O(1), erase/count O(total stored characters) | O(total stored characters) |
| Optimal | insert/erase/search/prefix count O(L) | O(total distinct prefix nodes) |

### Edge cases

- Repeated insertions increase both path and terminal counts.
- Erasing one copy must not remove other copies of the same word.
