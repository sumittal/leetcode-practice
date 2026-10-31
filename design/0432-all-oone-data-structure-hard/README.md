# 432. All O`one Data Structure

**Difficulty:** Hard  
**Tags:** Hash Table, Linked List, Design, Doubly-Linked List  
**Companies:** Nextdoor, Atlassian, LinkedIn, Optum, Uber, TikTok, Amazon, Apple, Meta, Microsoft, Google, Bloomberg  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/all-oone-data-structure/](https://leetcode.com/problems/all-oone-data-structure/)

## Problem

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the `AllOne` class:

- `AllOne()` Initializes the object of the data structure.
- `inc(String key)` Increments the count of the string `key` by `1`. If `key` does not exist in the data structure, insert it with count `1`.
- `dec(String key)` Decrements the count of the string `key` by `1`. If the count of `key` is `0` after the decrement, remove it from the data structure. It is guaranteed that `key` exists in the data structure before the decrement.
- `getMaxKey()` Returns one of the keys with the maximal count. If no element exists, return an empty string `""`.
- `getMinKey()` Returns one of the keys with the minimum count. If no element exists, return an empty string `""`.

**Note** that each function must run in `O(1)` average time complexity.

**Example 1:**

```

**Input**
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
**Output**
[null, null, null, "hello", "hello", null, "hello", "leet"]

**Explanation**
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

```

**Constraints:**

- `1 <= key.length <= 10`
- `key` consists of lowercase English letters.
- It is guaranteed that for each call to `dec`, `key` is existing in the data structure.
- At most `5 * 10^4` calls will be made to `inc`, `dec`, `getMaxKey`, and `getMinKey`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 432 All O`one Data Structure neetcode](https://www.youtube.com/results?search_query=leetcode+432+All+O%60one+Data+Structure+neetcode)

## Approach

### Intuition

Keep keys grouped by count in increasing order so the first and last buckets expose the minimum and maximum.

### Brute Force

Maintain key counts in a map and scan all keys whenever a minimum or maximum key is requested.

### Optimal

Maintain a doubly linked list of count buckets, with a set of keys at each count and a key-to-bucket map.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | inc O(1), dec O(1), getMinKey O(n), getMaxKey O(n) | O(unique keys) |
| Optimal | inc O(1), dec O(1), getMinKey O(1), getMaxKey O(1) | O(unique keys) |

### Edge cases

- Decrementing a key from count one removes it.
- An empty structure returns an empty string for either key query.
