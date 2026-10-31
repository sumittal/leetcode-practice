# 238. Product of Array Except Self

**Difficulty:** Medium  
**Tags:** Array, Prefix Sum  
**Companies:** ZS Associates, ThousandEyes, Asana, FreshWorks, PayPal, Avito, Uber, Okta, Amazon, Apple, Zoho, Microsoft, Nvidia, Bloomberg, Yandex (+15 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

```
**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

```

**Example 2:**

```
**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

```

**Constraints:**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Video Explanation

[Product of Array Except Self - Leetcode 238 - Python](https://www.youtube.com/watch?v=bNvIQI2wAjk)

## Approach

### Intuition

For each position, multiply the product of values to its left by the product of values to its right.

### Brute Force

For every index, multiply all elements except the one at that index.

### Optimal

Write prefix products into the output, then scan backward while multiplying in the suffix product. The output array is excluded from extra-space accounting.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) extra |
| Optimal | O(n) | O(1) extra |

### Edge cases

- A single element produces [1], the empty product.
- Zeros need no special branch: prefix and suffix products naturally produce zero outputs, including when exactly one input is zero.
