# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium  
**Tags:** Array, Two Pointers, Binary Search  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem

You are given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**.

Find **two** numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index<sub>1</sub>]` and `numbers[index<sub>2</sub>]` where `1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length`.

Return the indices of the two numbers `index<sub>1</sub>` and `index<sub>2</sub>` as an integer array `[index<sub>1</sub>, index<sub>2</sub>]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

**Example 1:**

```

**Input:** numbers = [2,7,11,15], target = 9
**Output:** [1,2]
**Explanation:** The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].

```

**Example 2:**

```

**Input:** numbers = [2,3,4], target = 6
**Output:** [1,3]
**Explanation:** The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].

```

**Example 3:**

```

**Input:** numbers = [-1,0], target = -1
**Output:** [1,2]
**Explanation:** The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].

```

**Constraints:**

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

## Video Explanation

[TWO SUM II - Amazon Coding Interview Question - Leetcode 167 - Python](https://www.youtube.com/watch?v=cQ1Oz4ckceM)

## Approach

### Intuition

Because values are sorted, moving one endpoint inward changes the sum predictably.

### Brute Force

Try every pair until their values sum to the target.

### Optimal

Start at both ends and discard the side that cannot produce the target.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n) | O(1) |

### Edge cases

- The pair may include the first or last element.
- Negative values are valid inputs.
