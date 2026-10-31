# 4. Median of Two Sorted Arrays

**Difficulty:** Hard  
**Tags:** Array, Binary Search, Divide and Conquer  
**Companies:** Rippling, Zenefits, Yahoo, Dropbox, Adobe, Goldman Sachs, Bloomberg, Amazon, Microsoft, Google, Okta, GE Healthcare, Meta, Autodesk, Cognizant (+26 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

```

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.00000
**Explanation:** merged array = [1,2,3] and median is 2.

```

**Example 2:**

```

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.50000
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Video Explanation

[Median of Two Sorted Arrays - Binary Search - Leetcode 4](https://www.youtube.com/watch?v=q6IEA26hvXc)

## Approach

### Intuition

A correct partition places half the combined values on each side, with every left value no greater than every right value.

### Brute Force

Merge both arrays and read the middle value or average of the two middle values.

### Optimal

Binary search a partition in the shorter array and derive the complementary partition in the other array.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(m+n) | O(m+n) |
| Optimal | O(log(min(m,n))) | O(1) |

### Edge cases

- One input array may be empty.
- The combined length may be odd or even.
