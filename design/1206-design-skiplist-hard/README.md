# 1206. Design Skiplist

**Difficulty:** Hard  
**Tags:** Linked List, Design  
**Companies:** Optiver, X, eBay, Pure Storage, Microsoft, Google, Meta, Amazon  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/design-skiplist/](https://leetcode.com/problems/design-skiplist/)

## Problem

Design a **Skiplist** without using any built-in libraries.

A **skiplist** is a data structure that takes `O(log(n))` time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

For example, we have a Skiplist containing `[30,40,50,60,70,90]` and we want to add `80` and `45` into it. The Skiplist works this way:

![](https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif)
Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than `O(n)`. It can be proven that the average time complexity for each operation is `O(log(n))` and space complexity is `O(n)`.

See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

Implement the `Skiplist` class:

- `Skiplist()` Initializes the object of the skiplist.
- `bool search(int target)` Returns `true` if the integer `target` exists in the Skiplist or `false` otherwise.
- `void add(int num)` Inserts the value `num` into the SkipList.
- `bool erase(int num)` Removes the value `num` from the Skiplist and returns `true`. If `num` does not exist in the Skiplist, do nothing and return `false`. If there exist multiple `num` values, removing any one of them is fine.

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

**Example 1:**

```

**Input**
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
**Output**
[null, null, null, null, false, null, true, false, true, false]

**Explanation**
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0);  // return False, 0 is not in skiplist.
skiplist.erase(1);  // return True
skiplist.search(1); // return False, 1 has already been erased.
```

**Constraints:**

- `0 <= num, target <= 2 * 10^4`
- At most `5 * 10^4` calls will be made to `search`, `add`, and `erase`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1206 Design Skiplist neetcode](https://www.youtube.com/results?search_query=leetcode+1206+Design+Skiplist+neetcode)

## Approach

### Intuition

Multiple forward levels let searches skip over many sorted values before descending to the next level.

### Brute Force

Keep values in a linked list and traverse from the head for each search, insertion, or removal.

### Optimal

Use randomized skip-list levels so expected searches and pointer updates visit logarithmically many nodes.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | search O(n), add O(n), erase O(n) | O(n) |
| Optimal | search O(log n) expected, add O(log n) expected, erase O(log n) expected | O(n) expected |

### Edge cases

- Duplicate values may be stored and erased one occurrence at a time.
- Searching or erasing an absent value does not modify the structure.
