# 300. Longest Increasing Subsequence

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Dynamic Programming, Longest Increasing Subsequence  
**Companies:** Samsung, PayPal, TikTok, Revolut, Squarepoint Capital, Huawei, ByteDance, Infosys, Microsoft, Morgan Stanley, Walmart Labs, Google, Amazon, Intuit, Bloomberg (+10 more)  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem

Given an integer array `nums`, return *the length of the longest **strictly increasing*** ***subsequence***.

**Example 1:**

```

**Input:** nums = [10,9,2,5,3,7,101,18]
**Output:** 4
**Explanation:** The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

```

**Example 2:**

```

**Input:** nums = [0,1,0,3,2,3]
**Output:** 4

```

**Example 3:**

```

**Input:** nums = [7,7,7,7,7,7,7]
**Output:** 1

```

**Constraints:**

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Video Explanation

[Longest Increasing Subsequence - Dynamic Programming - Leetcode 300](https://www.youtube.com/watch?v=cjWnW0hdF1Y)

## Approach

### Intuition

For each subsequence length, retain the smallest possible ending value to leave room for future values.

### Brute Force

Enumerate subsequences and keep the longest strictly increasing one.

### Optimal

Maintain patience-sorting tails and binary-search the first tail not smaller than each value.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n log n) | O(n) |

### Edge cases

- Equal values replace a tail and do not increase strict LIS length.
- The tails array is not itself necessarily a subsequence.
