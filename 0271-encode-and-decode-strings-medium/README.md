# 271. Encode and Decode Strings

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, String, Design  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/encode-and-decode-strings/](https://leetcode.com/problems/encode-and-decode-strings/)

## Problem

Create a codec that converts a list of strings into one string and later recovers the same values in order. The input may include empty strings or delimiter characters, so the encoding must preserve boundaries without changing any content.

**Example 1:**
- Input: `strs = ["lint", "code", "love", "you"]`
- Output: `decode(encode(strs)) = ["lint", "code", "love", "you"]`
- Explanation: Each string is restored exactly in its original position.

**Example 2:**
- Input: `strs = ["", "a#b"]`
- Output: `decode(encode(strs)) = ["", "a#b"]`
- Explanation: Length prefixes preserve both the empty value and the `#` inside the payload.

**Constraints:**
- The list may be empty.
- Strings may be empty and may contain any character.

## Video Explanation

[Encode and Decode Strings - Leetcode 271 - Python](https://www.youtube.com/watch?v=B1k_sxOSgv8)

## Approach

### Intuition

A delimiter alone is ambiguous when data can contain that delimiter; prefix each value with its character length.

### Brute Force

Escape separators before joining and unescape after splitting.

### Optimal

Encode each string as decimal length, `#`, then its contents; decode by reading the length before consuming exactly that many characters.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n + L) | O(n + L) |
| Optimal | O(L) | O(L) |

### Edge cases

- Empty list differs from a list containing an empty string.
- Payloads may contain `#` because decoding uses lengths, not delimiter search.
