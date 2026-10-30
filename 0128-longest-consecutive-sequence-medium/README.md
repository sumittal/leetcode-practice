# 128. Longest Consecutive Sequence

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Union-Find  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

```

**Input:** nums = [100,4,200,1,3,2]
**Output:** 4
**Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

**Example 2:**

```

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]
**Output:** 9

```

**Example 3:**

```

**Input:** nums = [1,0,1,2]
**Output:** 3

```

**Constraints:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Video Explanation

[Leetcode 128 - LONGEST CONSECUTIVE SEQUENCE](https://www.youtube.com/watch?v=P6RZZMu_maU)

## Approach

### Intuition

Only the start of each consecutive run needs to count forward; all other values in that run can be skipped.

### Brute Force

From every value, repeatedly check whether its successor exists and count the resulting run.

### Optimal

Put values in a set and expand only when value - 1 is absent, so every run is traversed once.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty input has a longest run of length zero.
- Duplicates do not lengthen a run because membership is tested in a set.
- Negative values and runs crossing zero need no special handling.
