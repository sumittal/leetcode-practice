# 677. Map Sum Pairs

**Difficulty:** Medium  
**Tags:** Hash Table, String, Design, Trie  
**Companies:** Akuna Capital, Flipkart  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/map-sum-pairs/](https://leetcode.com/problems/map-sum-pairs/)

## Problem

Design a map that allows you to do the following:

- Maps a string key to a given value.
- Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the `MapSum` class:

- `MapSum()` Initializes the `MapSum` object.
- `void insert(String key, int val)` Inserts the `key-val` pair into the map. If the `key` already existed, the original `key-value` pair will be overridden to the new one.
- `int sum(string prefix)` Returns the sum of all the pairs' value whose `key` starts with the `prefix`.

**Example 1:**

```

**Input**
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
**Output**
[null, null, 3, null, 5]

**Explanation**
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

```

**Constraints:**

- `1 <= key.length, prefix.length <= 50`
- `key` and `prefix` consist of only lowercase English letters.
- `1 <= val <= 1000`
- At most `50` calls will be made to `insert` and `sum`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 677 Map Sum Pairs neetcode](https://www.youtube.com/results?search_query=leetcode+677+Map+Sum+Pairs+neetcode)

## Approach

### Intuition

Every prefix node can cache the total value of keys passing through it.

### Brute Force

Store key values and scan all keys that start with the requested prefix.

### Optimal

Use a trie with prefix sums and apply only the value delta when a key is overwritten.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | insert O(1), sum O(n * L) | O(total key characters) |
| Optimal | insert O(L), sum O(L) | O(total key characters) |

### Edge cases

- Inserting an existing key replaces its previous contribution.
- An absent prefix has sum zero.
