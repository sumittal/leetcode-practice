# 373. Find K Pairs with Smallest Sums

**Difficulty:** Medium  
**Tags:** Array, Heap (Priority Queue)  
**Companies:** LinkedIn, Sprinklr, Uber, Amazon, Oracle, Google, Microsoft, Meta, Bloomberg  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/find-k-pairs-with-smallest-sums/](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## Problem

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return *the* `k` *pairs* `(u<sub>1</sub>, v<sub>1</sub>), (u<sub>2</sub>, v<sub>2</sub>), ..., (u<sub>k</sub>, v<sub>k</sub>)` *with the smallest sums*.

**Example 1:**

```

**Input:** nums1 = [1,7,11], nums2 = [2,4,6], k = 3
**Output:** [[1,2],[1,4],[1,6]]
**Explanation:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

```

**Example 2:**

```

**Input:** nums1 = [1,1,2], nums2 = [1,2,3], k = 2
**Output:** [[1,1],[1,1]]
**Explanation:** The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1` and `nums2` both are sorted in **non-decreasing order**.
- `1 <= k <= 10^4`
- `k <= nums1.length * nums2.length`

## Video Explanation

[YouTube search: Search YouTube for leetcode 373 Find K Pairs with Smallest Sums neetcode](https://www.youtube.com/results?search_query=leetcode+373+Find+K+Pairs+with+Smallest+Sums+neetcode)

## Approach

### Intuition

Each fixed first-array value forms a sorted row of pair sums.

### Brute Force

Generate every pair, sort by sum, and keep the first k.

### Optimal

Seed a min-heap with the first pair from up to k rows; after removing a pair, add the next pair in that row.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(m n log(m n)) | O(m n) |
| Optimal | O(k log(min(k, m))) | O(min(k, m)) |

### Edge cases

- If either array is empty or k is zero, return an empty list.
- If k exceeds the number of possible pairs, return every pair.
- Equal sums may be returned in any order.
