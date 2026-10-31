# 268. Missing Number

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting  
**Companies:** Arista Networks, Revolut, HCL, Nvidia, Bloomberg, Amazon, tcs, Microsoft, Google, Meta, Zoho, Salesforce, Infosys, Apple, IBM (+1 more)  
**Pattern:** Bit Manipulation  
**LeetCode:** [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

**Example 1:**

**Input:** nums = [3,0,1]

**Output:** 2

**Explanation:**

`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

**Input:** nums = [9,6,4,2,3,5,7,0,1]

**Output:** 8

**Explanation:**

`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Video Explanation

[Missing Number - Blind 75 - Leetcode 268 - Python](https://www.youtube.com/watch?v=WnPLSRLSANE)

## Approach

### Intuition

The expected sum from zero through n differs from the actual sum by exactly the missing value.

### Brute Force

Sort and compare each value with its expected index.

### Optimal

Subtract the array sum from n(n+1)/2.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- The missing value may be n.
- An empty list has missing value zero.
