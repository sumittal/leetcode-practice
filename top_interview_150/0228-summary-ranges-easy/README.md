# 228. Summary Ranges

**Difficulty:** Easy  
**Tags:** Array  
**Companies:** Yandex, VK, Tinkoff, Netflix, Google, Bloomberg, Amazon, Microsoft, Meta  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/summary-ranges/](https://leetcode.com/problems/summary-ranges/)

## Problem

You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Example 1:**

```

**Input:** nums = [0,1,2,4,5,7]
**Output:** ["0->2","4->5","7"]
**Explanation:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

```

**Example 2:**

```

**Input:** nums = [0,2,3,4,6,8,9]
**Output:** ["0","2->4","6","8->9"]
**Explanation:** The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

```

**Constraints:**

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.

## Video Explanation

[YouTube search: Search YouTube for leetcode 228 Summary Ranges neetcode](https://www.youtube.com/results?search_query=leetcode+228+Summary+Ranges+neetcode)

## Approach

### Intuition

A range continues while each next sorted value is exactly one greater than the previous value.

### Brute Force

For every input value, search ahead to determine the end of its consecutive run.

### Optimal

Walk each run once and format its start and end as either one number or a range.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- An empty input returns no ranges.
- A singleton run is formatted as one number.
- The input is sorted and contains unique values.
