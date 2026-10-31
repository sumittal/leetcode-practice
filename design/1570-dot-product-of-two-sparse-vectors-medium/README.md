# 1570. Dot Product of Two Sparse Vectors

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Two Pointers, Design, Linear Algebra  
**Companies:** Meta, Nuro, General Motors, Nvidia, Bloomberg, LinkedIn, TikTok, Apple, Microsoft, Amazon, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/dot-product-of-two-sparse-vectors/](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/)

## Problem

Represent integer vectors whose length may be large but whose nonzero entries are few, then compute their dot product. Example 1: [1,0,0,2,3] dotted with [0,3,0,4,0] is 8. Example 2: [-1,0,0,0,0] dotted with [0,0,0,0,2] is 0. Constraints: both vectors have equal length, and most entries may be zero.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1570 Dot Product of Two Sparse Vectors neetcode](https://www.youtube.com/results?search_query=leetcode+1570+Dot+Product+of+Two+Sparse+Vectors+neetcode)

## Approach

### Intuition

Only positions nonzero in both vectors can contribute to the sum.

### Brute Force

Store both full vectors and multiply corresponding entries across the entire length.

### Optimal

Store only nonzero index-value pairs and iterate the smaller sparse map while looking up matching indices in the other.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | initialization O(n), dotProduct O(n) | O(n) |
| Optimal | initialization O(n), dotProduct O(min(a,b)) average | O(nonzero entries) |

### Edge cases

- A vector with no nonzero values always yields a zero dot product.
- Negative values contribute with their signed product.
