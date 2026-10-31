# 45. Jump Game II

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Greedy  
**Companies:** Groupon, HashedIn, Zoho, Grab, ServiceNow, PhonePe, eBay, Nutanix, Amazon, Meesho, Microsoft, Flipkart, TikTok, Google, Bloomberg (+13 more)  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/jump-game-ii/](https://leetcode.com/problems/jump-game-ii/)

## Problem

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return *the minimum number of jumps to reach index* `n - 1`. The test cases are generated such that you can reach index `n - 1`.

**Example 1:**

```

**Input:** nums = [2,3,1,1,4]
**Output:** 2
**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```

**Input:** nums = [2,3,0,1,4]
**Output:** 2

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Video Explanation

[Jump Game II - Greedy - Leetcode 45 - Python](https://www.youtube.com/watch?v=dJ7sWiOoK7g)

## Approach

### Intuition

Treat every index reachable in the current jump count as one layer and find the next layer's farthest boundary.

### Brute Force

Use DP to try every reachable next index from each position.

### Optimal

Scan each greedy reachability layer once, extending its farthest endpoint and counting a jump at each boundary.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A one-element array needs zero jumps.
- The problem guarantees the last index is reachable.
