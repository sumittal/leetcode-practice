# 604. Design Compressed String Iterator

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Easy  
**Tags:** Array, String, Design, Iterator  
**Companies:** Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-compressed-string-iterator/](https://leetcode.com/problems/design-compressed-string-iterator/)

## Problem

Iterate lazily through a string encoded as repeated character/count pairs. Example 1: the encoding A2B1 yields A, A, B, then a space after exhaustion. Example 2: a run count of zero contributes no output, and an exhausted iterator still returns a space. Constraints: characters are letters, counts are nonnegative decimal integers, and the encoding is valid.

## Video Explanation

[YouTube search: Search YouTube for leetcode 604 Design Compressed String Iterator neetcode](https://www.youtube.com/results?search_query=leetcode+604+Design+Compressed+String+Iterator+neetcode)

## Approach

### Intuition

Only the current run and its remaining count are needed to produce the next character.

### Brute Force

Expand every run into a complete string before serving iterator calls.

### Optimal

Parse run pairs once and advance through them only when the current count is exhausted.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(expanded length), next O(1) | O(expanded length) |
| Optimal | construction O(encoded length), next O(1) amortized, hasNext O(1) | O(number of runs) |

### Edge cases

- A run count may contain multiple digits.
- next returns a single space when no characters remain.
