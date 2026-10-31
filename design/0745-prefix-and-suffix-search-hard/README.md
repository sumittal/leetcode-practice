# 745. Prefix and Suffix Search

**Difficulty:** Hard  
**Tags:** Array, Hash Table, String, Design, Trie  
**Companies:** Meta, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/prefix-and-suffix-search/](https://leetcode.com/problems/prefix-and-suffix-search/)

## Problem

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the `WordFilter` class:

- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `f(string pref, string suff)` Returns *the index of the word in the dictionary,* which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return **the largest** of them. If there is no such word in the dictionary, return `-1`.

**Example 1:**

```

**Input**
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
**Output**
[null, 0]
**Explanation**
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

```

**Constraints:**

- `1 <= words.length <= 10^4`
- `1 <= words[i].length <= 7`
- `1 <= pref.length, suff.length <= 7`
- `words[i]`, `pref` and `suff` consist of lowercase English letters only.
- At most `10^4` calls will be made to the function `f`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 745 Prefix and Suffix Search neetcode](https://www.youtube.com/results?search_query=leetcode+745+Prefix+and+Suffix+Search+neetcode)

## Approach

### Intuition

A query can be answered directly when every prefix/suffix pair maps to its latest word index.

### Brute Force

Scan words backward until one matches both the requested prefix and suffix.

### Optimal

Precompute every word prefix/suffix combination and overwrite its map entry as indices increase.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | f O(n * L) | O(total characters) |
| Optimal | construction O(n * L^2), f O(1) | O(n * L^2) |

### Edge cases

- Empty prefix and suffix match every word.
- If several words match, return the greatest input index.
