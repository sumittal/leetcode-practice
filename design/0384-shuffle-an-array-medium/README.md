# 384. Shuffle an Array

**Difficulty:** Medium  
**Tags:** Array, Math, Design, Randomized  
**Companies:** Uber, LinkedIn, Goldman Sachs, Google, Meta, Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/shuffle-an-array/](https://leetcode.com/problems/shuffle-an-array/)

## Problem

Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be **equally likely** as a result of the shuffling.

Implement the `Solution` class:

- `Solution(int[] nums)` Initializes the object with the integer array `nums`.
- `int[] reset()` Resets the array to its original configuration and returns it.
- `int[] shuffle()` Returns a random shuffling of the array.

**Example 1:**

```

**Input**
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
**Output**
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

**Explanation**
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

```

**Constraints:**

- `1 <= nums.length <= 50`
- `-10^6 <= nums[i] <= 10^6`
- All the elements of `nums` are **unique**.
- At most `10^4` calls **in total** will be made to `reset` and `shuffle`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 384 Shuffle an Array neetcode](https://www.youtube.com/results?search_query=leetcode+384+Shuffle+an+Array+neetcode)

## Approach

### Intuition

A uniformly random permutation is produced by choosing the next element from the remaining suffix.

### Brute Force

Generate all permutations and select one uniformly at random.

### Optimal

Copy the original array and perform an in-place Fisher-Yates shuffle on the copy.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | reset O(n), shuffle O(n!) | O(n!) |
| Optimal | reset O(n), shuffle O(n) | O(n) |

### Edge cases

- Reset always returns the original ordering.
- A shuffled result contains every original element exactly once.
