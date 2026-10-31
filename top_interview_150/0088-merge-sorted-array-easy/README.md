# 88. Merge Sorted Array

**Difficulty:** Easy  
**Tags:** Array, Two Pointers, Sorting  
**Companies:** Squarespace, Meta, Avito, EPAM Systems, Hubspot, HCL, Bloomberg, tcs, Microsoft, Zoho, Swiggy, Google, persistent systems, AMD, Amazon (+19 more)  
**Pattern:** Two Pointers  
**LeetCode:** [https://leetcode.com/problems/merge-sorted-array/](https://leetcode.com/problems/merge-sorted-array/)

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array* `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example 1:**

```

**Input:** nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
**Output:** [1,2,2,3,5,6]
**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

```

**Example 2:**

```

**Input:** nums1 = [1], m = 1, nums2 = [], n = 0
**Output:** [1]
**Explanation:** The arrays we are merging are [1] and [].
The result of the merge is [1].

```

**Example 3:**

```

**Input:** nums1 = [0], m = 0, nums2 = [1], n = 1
**Output:** [1]
**Explanation:** The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

```

**Constraints:**

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

**Follow up:** Can you come up with an algorithm that runs in `O(m + n)` time?

## Video Explanation

[Merge Sorted Array - Leetcode 88 - Python](https://www.youtube.com/watch?v=P1Ic85RarKY)

## Approach

### Intuition

Fill the output from the right so values already in nums1 are not overwritten before comparison.

### Brute Force

Copy nums1's initialized prefix, concatenate nums2, and sort the destination.

### Optimal

Compare the largest remaining values and write each into the last free slot, moving backward until nums2 is exhausted.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((m+n) log(m+n)) | O(m) |
| Optimal | O(m+n) | O(1) |

### Edge cases

- Either input can be empty.
- Equal values may be placed in either order.
- The initialized prefix of nums1 must remain available until consumed.
