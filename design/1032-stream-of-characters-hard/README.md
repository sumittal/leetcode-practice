# 1032. Stream of Characters

**Difficulty:** Hard  
**Tags:** Array, String, Design, Trie, Data Stream, Aho–Corasick Algorithm  
**Companies:** Jane Street, Google, Meta, Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/stream-of-characters/](https://leetcode.com/problems/stream-of-characters/)

## Problem

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings `words`.

For example, if `words = ["abc", "xyz"]` and the stream added the four characters (one by one) `'a'`, `'x'`, `'y'`, and `'z'`, your algorithm should detect that the suffix `"xyz"` of the characters `"axyz"` matches `"xyz"` from `words`.

Implement the `StreamChecker` class:

- `StreamChecker(String[] words)` Initializes the object with the strings array `words`.
- `boolean query(char letter)` Accepts a new character from the stream and returns `true` if any non-empty suffix from the stream forms a word that is in `words`.

**Example 1:**

```

**Input**
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
**Output**
[null, false, false, false, true, false, true, false, false, false, false, false, true]

**Explanation**
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist

```

**Constraints:**

- `1 <= words.length <= 2000`
- `1 <= words[i].length <= 200`
- `words[i]` consists of lowercase English letters.
- `letter` is a lowercase English letter.
- At most `4 * 10^4` calls will be made to query.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1032 Stream of Characters neetcode](https://www.youtube.com/results?search_query=leetcode+1032+Stream+of+Characters+neetcode)

## Approach

### Intuition

A query asks whether any stored word is a suffix of the stream, so reading both words and stream backward shares useful prefixes.

### Brute Force

Append each letter and compare the accumulated suffix against every word.

### Optimal

Store reversed words in a trie and traverse at most the longest word length from a bounded history deque.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | query O(number of words times maximum word length) | O(stream length) |
| Optimal | query O(maximum word length), construction O(total word characters) | O(total word characters + maximum word length) |

### Edge cases

- A word may match immediately after one query.
- The retained history never needs to exceed the longest dictionary word.
