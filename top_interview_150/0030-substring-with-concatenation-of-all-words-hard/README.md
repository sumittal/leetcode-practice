# 30. Substring with Concatenation of All Words

**Difficulty:** Hard  
**Tags:** Hash Table, String, Sliding Window  
**Companies:** Samsung, Texas Instruments, eBay, Bloomberg, Amazon, Google, Microsoft, Infosys, Meta, Apple  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/substring-with-concatenation-of-all-words/](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## Problem

You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of *the starting indices* of all the concatenated substrings in `s`. You can return the answer in **any order**.

**Example 1:**

**Input:** s = "barfoothefoobarman", words = ["foo","bar"]

**Output:** [0,9]

**Explanation:**

The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

**Example 2:**

**Input:** s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

**Output:** []

**Explanation:**

There is no concatenated substring.

**Example 3:**

**Input:** s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

**Output:** [6,9,12]

**Explanation:**

The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.
The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.
The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.

**Constraints:**

- `1 <= s.length <= 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters.

## Video Explanation

[YouTube search: Search YouTube for leetcode 30 Substring with Concatenation of All Words neetcode](https://www.youtube.com/results?search_query=leetcode+30+Substring+with+Concatenation+of+All+Words+neetcode)

## Approach

### Intuition

Every valid concatenation contains the same fixed number of equal-width words, so each width-aligned window can be checked with word frequencies.

### Brute Force

Try every starting index and compare its next totalLength characters against every permutation of words.

### Optimal

For each word-width offset, slide by whole words while tracking counts and shrink whenever a word is overrepresented.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n * wordCount!) | O(wordCount) |
| Optimal | O(n * wordWidth) | O(wordCount) |

### Edge cases

- An empty words list has no concatenation.
- Repeated words require frequency counts rather than a set.
- Matches can overlap and answers are returned in index order.
