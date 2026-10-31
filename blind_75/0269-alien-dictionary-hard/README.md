# 269. Alien Dictionary

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Array, String, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph  
**Companies:** Pocket Gems, Uber, X, Wix, Snap, Airbnb, Okta, Coupang, Waymo, Nuro, Meta, TikTok, eBay, Intuit, Amazon (+4 more)  
**Pattern:** Advanced Graphs  
**LeetCode:** [https://leetcode.com/problems/alien-dictionary/](https://leetcode.com/problems/alien-dictionary/)

## Problem

A list of words is sorted according to an unknown alphabet, but the character order is not provided. Infer an order consistent with the list by using the first position where each adjacent pair differs, and return a valid ordering of all observed characters or an empty string when no ordering exists.

**Example 1:**
- Input: `words = ["wrt","wrf","er","ett","rftt"]`
- Output: `"wertf"`
- Explanation: The adjacent comparisons imply `w < e`, `r < t`, `t < f`, and `e < r`.

**Example 2:**
- Input: `words = ["z","x"]`
- Output: `"zx"`
- Explanation: The only ordering constraint is that `z` comes before `x`.

**Constraints:**
- `1 <= words.length <= 100`.
- Words contain lowercase English letters.
- A longer word before its exact prefix is invalid; cycles have no valid order.

## Video Explanation

[Alien Dictionary - Topological Sort - Leetcode 269 - Python](https://www.youtube.com/watch?v=6kTZYvNNyps)

## Approach

### Intuition

Adjacent sorted words reveal precedence only at their first differing character.

### Brute Force

Try permutations of all observed characters and validate each adjacent word pair.

### Optimal

Build precedence edges, reject invalid prefixes, then topologically sort all observed characters.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(V!*N*L) | O(V) |
| Optimal | O(total chars + V + E) | O(V+E) |

### Edge cases

- A longer word before its exact prefix is invalid.
- Return any valid topological order when several exist.
