# 433. Minimum Genetic Mutation

**Difficulty:** Medium  
**Tags:** Hash Table, String, Breadth-First Search, Bidirectional Search  
**Companies:** X, Amazon, Bloomberg, Google, Microsoft, Meta  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/minimum-genetic-mutation/](https://leetcode.com/problems/minimum-genetic-mutation/)

## Problem

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

- For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return *the minimum number of mutations needed to mutate from* `startGene`* to* `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

**Example 1:**

```

**Input:** startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
**Output:** 1

```

**Example 2:**

```

**Input:** startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
**Output:** 2

```

**Constraints:**

- `0 <= bank.length <= 10`
- `startGene.length == endGene.length == bank[i].length == 8`
- `startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 433 Minimum Genetic Mutation neetcode](https://www.youtube.com/results?search_query=leetcode+433+Minimum+Genetic+Mutation+neetcode)

## Approach

### Intuition

A valid mutation changes exactly one gene character, so the bank defines the vertices and one-character mutations define edges.

### Brute Force

Try every sequence of gene strings and retain the shortest one that reaches the target.

### Optimal

Run BFS from the start, generating each one-character mutation and enqueueing only unseen strings in the bank.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(B) |
| Optimal | O(B * L * A) | O(B) |

### Edge cases

- The target already equals the start, requiring zero mutations.
- A distinct target not in the bank is unreachable.
- Only the four DNA bases are valid mutations.
