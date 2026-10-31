# 53. Maximum Subarray

**Difficulty:** Medium  
**Tags:** Array, Divide and Conquer, Dynamic Programming  
**Companies:** Upstart, Squarepoint Capital, Target, Wix, tcs, Tekion, LinkedIn, Infosys, Mastercard, Microsoft, Accenture, Nvidia, Zomato, Amazon, Vimeo (+41 more)  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

**Example 1:**

```

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

```

**Example 2:**

```

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

```

**Example 3:**

```

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Video Explanation

[Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python](https://www.youtube.com/watch?v=5WZl3MMT0Eg)

## Approach

### Intuition

A best subarray ending here either starts here or extends the previous best ending here.

### Brute Force

Evaluate every contiguous range sum.

### Optimal

Kadane's recurrence tracks the best sum ending at each position and the global maximum.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- All-negative input returns its largest single value.
- A negative running sum is discarded before the next value.
