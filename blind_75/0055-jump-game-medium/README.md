# 55. Jump Game

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Greedy  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)

## Problem

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or* `false`* otherwise*.

**Example 1:**

```

**Input:** nums = [2,3,1,1,4]
**Output:** true
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```

**Input:** nums = [3,2,1,0,4]
**Output:** false
**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Video Explanation

[Jump Game - Greedy - Leetcode 55](https://www.youtube.com/watch?v=Yan0cv2cLy8)

## Approach

### Intuition

Track the furthest index reachable so far; any index beyond it cannot be visited.

### Brute Force

Search all jump sequences from index zero.

### Optimal

Scan reachable indices and extend the farthest boundary using each jump length.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- A single-element array is already at the destination.
- Stop once the scan passes the reachable boundary.
