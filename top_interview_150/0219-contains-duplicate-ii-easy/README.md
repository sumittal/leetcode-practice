# 219. Contains Duplicate II

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Sliding Window  
**Companies:** Arista Networks, Airbnb, Netflix, Meta, Accenture, tcs, Bloomberg, Adobe, Google, Amazon, Microsoft, Zoho  
**Pattern:** Sliding Window  
**LeetCode:** [https://leetcode.com/problems/contains-duplicate-ii/](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices*** `i`* and* `j`* in the array such that* `nums[i] == nums[j]`* and* `abs(i - j) <= k`.

**Example 1:**

```

**Input:** nums = [1,2,3,1], k = 3
**Output:** true

```

**Example 2:**

```

**Input:** nums = [1,0,1,1], k = 1
**Output:** true

```

**Example 3:**

```

**Input:** nums = [1,2,3,1,2,3], k = 2
**Output:** false

```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Video Explanation

[Contains Duplicate II - Leetcode 219 - Python](https://www.youtube.com/watch?v=ypn0aZ0nrL4)

## Approach

### Intuition

A duplicate is nearby when the earlier copy remains in the most recent k-index window.

### Brute Force

Compare every pair of equal values and check their index distance.

### Optimal

Maintain a set of the last at most k values and test each new value before adding it.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(k) |

### Edge cases

- A nonpositive k cannot contain a valid pair.
- A one-element array has no duplicate pair.
- Remove an item once it falls more than k indices behind.
