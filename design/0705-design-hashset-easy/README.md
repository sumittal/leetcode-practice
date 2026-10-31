# 705. Design HashSet

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Linked List, Design, Hash Function  
**Companies:** Wix, Google, Meta, Bloomberg, Amazon  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/design-hashset/](https://leetcode.com/problems/design-hashset/)

## Problem

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

**Example 1:**

```

**Input**
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
**Output**
[null, null, null, true, false, null, true, null, false]

**Explanation**
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

**Constraints:**

- `0 <= key <= 10^6`
- At most `10^4` calls will be made to `add`, `remove`, and `contains`.

## Video Explanation

[Design HashSet - Leetcode 705 - Python](https://www.youtube.com/watch?v=VymjPQUXjL8)

## Approach

### Intuition

Hash each integer into a bucket and keep each key at most once within that bucket.

### Brute Force

Store all keys in one list and scan it for membership, insertion, and removal.

### Optimal

Use separate chaining across a fixed bucket array and search only the selected bucket.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add O(n), remove O(n), contains O(n) | O(n) |
| Optimal | add O(1) average, remove O(1) average, contains O(1) average | O(n + bucket count) |

### Edge cases

- Adding an existing key leaves the set unchanged.
- Removing a missing key is a no-op.
