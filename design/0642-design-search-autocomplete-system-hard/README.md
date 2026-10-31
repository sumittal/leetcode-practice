# 642. Design Search Autocomplete System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** String, Depth-First Search, Design, Trie, Sorting, Heap (Priority Queue), Data Stream  
**Companies:** Roblox, MongoDB, Pinterest, Netflix, Citadel, Cisco, Microsoft, Bloomberg, Uber, Meta, Google, Amazon  
**Pattern:** String  
**LeetCode:** [https://leetcode.com/problems/design-search-autocomplete-system/](https://leetcode.com/problems/design-search-autocomplete-system/)

## Problem

Build an autocomplete tool that returns the three most frequent stored sentences matching the text typed so far, breaking equal-frequency ties alphabetically. Typing # saves the current text as a sentence and clears the query. Example 1: with "i love you" occurring 5 times, "island" 3 times, and "i love leetcode" 2 times, typing i returns those three in that order. Example 2: then typing a space returns ["i love you", "i love leetcode"]. Constraints: input characters are lowercase letters, spaces, or #; stored counts and sentence lengths fit in memory.

## Video Explanation

[YouTube search: Search YouTube for leetcode 642 Design Search Autocomplete System neetcode](https://www.youtube.com/results?search_query=leetcode+642+Design+Search+Autocomplete+System+neetcode)

## Approach

### Intuition

Store sentence candidates at every prefix so a query only sorts sentences that match the typed prefix.

### Brute Force

Scan every sentence, filter by prefix, and sort all matches for each typed character.

### Optimal

Map each prefix to its matching sentences and rank only that prefix's candidates by frequency and lexical order.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | input O(S log S), initialization O(S) | O(total sentence characters) |
| Optimal | input O(P log P), initialization O(total sentence characters) | O(total sentence prefixes) |

### Edge cases

- Typing # commits the sentence and returns an empty suggestion list.
- A prefix with no stored matches returns an empty list.
