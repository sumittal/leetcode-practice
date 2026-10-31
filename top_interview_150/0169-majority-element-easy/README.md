# 169. Majority Element

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm  
**Companies:** Zenefits, Adobe, Odoo, Accenture, Qualcomm, Bloomberg, tcs, Microsoft, Amazon, Google, Meta, Autodesk, Cognizant, Infosys, Morgan Stanley (+5 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/majority-element/](https://leetcode.com/problems/majority-element/)

## Problem

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
**Input:** nums = [3,2,3]
**Output:** 3

```

**Example 2:**

```
**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The input is generated such that a majority element will exist in the array.

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Video Explanation

[Majority Element - Leetcode 169 - Python](https://www.youtube.com/watch?v=7pnhv842keE)

## Approach

### Intuition

The majority occurs more than all other values combined, so pairwise cancellation cannot remove every copy of it.

### Brute Force

Count each candidate value and return one whose frequency exceeds half the array.

### Optimal

Use Boyer-Moore voting: cancel different values and retain a candidate with a positive balance.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- The input guarantees a majority element.
- A single-element array is its own majority.
- The final candidate need not be recounted because of the guarantee.
