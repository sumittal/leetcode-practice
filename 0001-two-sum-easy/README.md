# 1. Two Sum

**Difficulty:** Easy  
**Tags:** Array, Hash Table  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem

You are given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

**Input:** `nums = [2,7,11,15], target = 9`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `2 + 7 = 9`, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Example 2:**

**Input:** `nums = [3,2,4], target = 6`

**Output:** `[1,2]`

**Explanation:**

The sum of `nums[1]` and `nums[2]` is `2 + 4 = 6`, which equals the target. Therefore, the indices `[1, 2]` are returned.

**Example 3:**

**Input:** `nums = [3,3], target = 6`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `3 + 3 = 6`, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## Video Explanation

[Two Sum - Leetcode 1 - HashMap - Python](https://www.youtube.com/watch?v=KLlXCFG5TnA)

## Approach

### Intuition

For each value, the only useful partner is its complement (`target - value`). Remember values already seen so each pair can be found in one pass.

### Brute Force

Try every pair of indices and return the first pair whose values sum to the target.

### Optimal

Scan once while mapping each value to its index. Check for the complement before recording the current value so an element is never paired with itself.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(n) |

### Edge cases

- Duplicate values can form the answer; check the complement before inserting the current value.
- Negative values and a negative target work with the same complement calculation.
