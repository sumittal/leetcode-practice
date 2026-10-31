# 152. Maximum Product Subarray

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming  
**Companies:** Delhivery, Adobe, LinkedIn, Siemens, Morgan Stanley, tcs, HashedIn, Swiggy, DE Shaw, Qualcomm, Amazon, Bloomberg, Google, Infosys, ByteDance (+7 more)  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

**​​​​​​​Example 1:**

```

**Input:** nums = [2,3,-2,4]
**Output:** 6
**Explanation:** [2,3] has the largest product 6.

```

**Example 2:**

```

**Input:** nums = [-2,0,-1]
**Output:** 0
**Explanation:** The result cannot be 2, because [-2,-1] is not a subarray.

```

**Constraints:**

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## Video Explanation

[Maximum Product Subarray - Dynamic Programming - Leetcode 152](https://www.youtube.com/watch?v=lXVy6YWFcRM)

## Approach

### Intuition

A negative value swaps the roles of the largest and smallest products ending here.

### Brute Force

Compute every contiguous subarray product.

### Optimal

Track maximum and minimum ending products because a negative can turn either into the other.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- Zero resets products for the next segment.
- A single negative value is itself a valid maximum.
