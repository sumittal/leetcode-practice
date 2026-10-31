# 211. Design Add and Search Words Data Structure

**Difficulty:** Medium  
**Tags:** String, Depth-First Search, Design, Trie  
**Companies:** Datadog, Snowflake, TikTok, Snap, Apple, Amazon, Atlassian, Microsoft, Oracle, Meta, Google, Bloomberg  
**Pattern:** Tries  
**LeetCode:** [https://leetcode.com/problems/design-add-and-search-words-data-structure/](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Problem

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

**Example:**

```

**Input**
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
**Output**
[null,null,null,null,false,true,true,true]

**Explanation**
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

```

**Constraints:**

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Video Explanation

[Design Add and Search Words Data Structure - Leetcode 211 - Python](https://www.youtube.com/watch?v=BTf05gs_8iU)

## Approach

### Intuition

A trie handles fixed letters directly; a dot branches over every child at that position.

### Brute Force

Store all words and test each against the query pattern.

### Optimal

Traverse trie edges; recursively branch over children only for wildcard positions.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(W*L) per search | O(total chars) |
| Optimal | O(L) normally, O(26^d) for d wildcards | O(L) search stack |

### Edge cases

- A wildcard must match exactly one character.
- A search succeeds only at a terminal node.
