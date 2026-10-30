# 23. Merge k Sorted Lists

**Difficulty:** Hard  
**Tags:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort, Tournament Sort  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]
**Output:** [1,1,2,3,4,4,5,6]
**Explanation:** The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

```

**Example 2:**

```

**Input:** lists = []
**Output:** []

```

**Example 3:**

```

**Input:** lists = [[]]
**Output:** []

```

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10^4`.

## Video Explanation

[Merge K Sorted Lists - Leetcode 23 - Python](https://www.youtube.com/watch?v=q5a5OiGbT6Q)

## Approach

### Intuition

The next output node is the smallest current head among all nonempty lists.

### Brute Force

Collect all node values, sort them, and build a merged list.

### Optimal

Keep one current node per list in a min-heap, repeatedly pop the smallest and push its successor. Divide and conquer is an alternative with O(n log k) time.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(n log k) | O(k) heap |

### Edge cases

- An empty collection or a collection of empty lists returns None.
- The heap tuple uses a list index to break equal-value ties because ListNode instances are not orderable.
- Push a successor only after removing its predecessor from the heap.
