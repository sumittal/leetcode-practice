# 303. Range Sum Query - Immutable

**Difficulty:** Easy  
**Tags:** Array, Design, Prefix Sum  
**Companies:** Infosys, Meta, Amazon, Bloomberg, tcs, Google, Microsoft  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/range-sum-query-immutable/](https://leetcode.com/problems/range-sum-query-immutable/)

## Problem

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

**Example 1:**

```

**Input**
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
**Output**
[null, 1, -1, -3]

**Explanation**
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

## Video Explanation

[Range Sum Query Immutable - Leetcode 303 - Python](https://www.youtube.com/watch?v=2pndAmo_sMA)

## Approach

### Intuition

Prefix sums let a range total be found by subtracting the sum before its left endpoint.

### Brute Force

Add every element from left through right for each query.

### Optimal

Precompute cumulative sums with a leading zero and subtract two prefix entries per query.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | sumRange O(n) | O(1) |
| Optimal | initialization O(n), sumRange O(1) | O(n) |

### Edge cases

- A one-element interval returns that element.
- Negative numbers are handled by the same prefix subtraction.
