# 2336. Smallest Number in Infinite Set

**Difficulty:** Medium  
**Tags:** Hash Table, Design, Heap (Priority Queue), Ordered Set  
**Companies:** Amazon, Meta, Microsoft, Bloomberg, Google  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/smallest-number-in-infinite-set/](https://leetcode.com/problems/smallest-number-in-infinite-set/)

## Problem

You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:

- `SmallestInfiniteSet()` Initializes the **SmallestInfiniteSet** object to contain **all** positive integers.
- `int popSmallest()` **Removes** and returns the smallest integer contained in the infinite set.
- `void addBack(int num)` **Adds** a positive integer `num` back into the infinite set, if it is **not** already in the infinite set.

**Example 1:**

```

**Input**
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
**Output**
[null, null, 1, 2, 3, null, 1, 4, 5]

**Explanation**
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

```

**Constraints:**

- `1 <= num <= 1000`
- At most `1000` calls will be made **in total** to `popSmallest` and `addBack`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2336 Smallest Number in Infinite Set neetcode](https://www.youtube.com/results?search_query=leetcode+2336+Smallest+Number+in+Infinite+Set+neetcode)

## Approach

### Intuition

A pointer represents the untouched infinite suffix, while a min-heap stores smaller numbers that were added back.

### Brute Force

Maintain an explicit set of all currently available positive integers and scan for its minimum.

### Optimal

Return the next pointer value unless a min-heap contains a smaller restored number; use a set to avoid duplicate heap entries.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | popSmallest O(n), addBack O(1) | O(n) |
| Optimal | popSmallest O(log n), addBack O(log n) | O(number of restored values) |

### Edge cases

- Adding back a number already available makes no change.
- Numbers at or beyond the pointer cannot have been removed from the infinite suffix.
