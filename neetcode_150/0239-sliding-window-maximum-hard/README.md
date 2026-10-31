# 239. Sliding Window Maximum

**Difficulty:** Hard  
**Tags:** Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue, Range Minimum/Maximum Query  
**Companies:** Citadel, Zenefits, Cohesity, blinkit, LINE, Nutanix, Zepto, Verily, Expedia, Aurora, Oracle, ServiceNow, DE Shaw, Faire, Booking.com (+33 more)  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

## Problem

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

**Example 1:**

```

**Input:** nums = [1,3,-1,-3,5,3,6,7], k = 3
**Output:** [3,3,5,5,6,7]
**Explanation:**
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
 1 [3  -1  -3] 5  3  6  7       **3**
 1  3 [-1  -3  5] 3  6  7      ** 5**
 1  3  -1 [-3  5  3] 6  7       **5**
 1  3  -1  -3 [5  3  6] 7       **6**
 1  3  -1  -3  5 [3  6  7]      **7**

```

**Example 2:**

```

**Input:** nums = [1], k = 1
**Output:** [1]

```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Video Explanation

[Sliding Window Maximum - Monotonic Queue - Leetcode 239](https://www.youtube.com/watch?v=DfljaUwZsOk)

## Approach

### Intuition

A decreasing deque keeps only candidates that could still become a window maximum.

### Brute Force

Take the maximum independently in every length-k slice.

### Optimal

Store candidate indices in a monotonic decreasing deque, expiring indices outside the window.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nk) | O(1) besides the output |
| Optimal | O(n) | O(k) |

### Edge cases

- A window of size one returns the input unchanged.
- A window covering the whole array produces one maximum.
