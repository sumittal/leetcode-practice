# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Tags:** Array, Two Pointers  
**Companies:** Wissen Technology, Bloomberg, Microsoft, tcs, Meta, Capgemini, Accenture, Google, Siemens, Amazon, Myntra, Deloitte, Cognizant, Morgan Stanley, Cisco (+8 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of *unique elements* in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

```

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

```

**Input:** nums = [1,1,2]
**Output:** 2, nums = [1,2,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

**Example 2:**

```

**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

**Constraints:**

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

## Video Explanation

[Remove Duplicates from Sorted Array - Leetcode 26 - Python](https://www.youtube.com/watch?v=DEJAZBq0FDA)

## Approach

### Intuition

In a sorted array each distinct value appears in one contiguous run, so one representative per run is enough.

### Brute Force

Create a new list containing only values different from the previous value.

### Optimal

Keep a write pointer and copy a value only when it differs from the last kept value.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) | O(n) |
| Optimal | O(n) | O(1) |

### Edge cases

- An empty or one-element array needs no compaction.
- All values may be equal.
- Only the returned prefix is significant.
