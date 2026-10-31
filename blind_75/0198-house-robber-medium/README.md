# 198. House Robber

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

**Example 1:**

```

**Input:** nums = [1,2,3,1]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

**Example 2:**

```

**Input:** nums = [2,7,9,3,1]
**Output:** 12
**Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Video Explanation

[House Robber -  Leetcode 198 - Python Dynamic Programming](https://www.youtube.com/watch?v=73r3KWiEvyk)

## Approach

### Intuition

At each house, either skip it or take it plus the best amount two positions back.

### Brute Force

Try every subset that contains no adjacent indices.

### Optimal

Maintain best totals through the previous and current houses.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- One house is the only possible nonempty choice.
- Taking a house excludes its immediate neighbor.
