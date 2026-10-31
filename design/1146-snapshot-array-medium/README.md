# 1146. Snapshot Array

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Binary Search, Design, Persistent Data Structure  
**Companies:** MongoDB, Verkada, Coupang, TikTok, Rubrik, Apple, Databricks, Aurora, Nutanix, Snowflake, Netflix, OpenAI, Google, Amazon, Microsoft (+2 more)  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/snapshot-array/](https://leetcode.com/problems/snapshot-array/)

## Problem

Implement a SnapshotArray that supports the following interface:

- `SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**.
- `void set(index, val)` sets the element at the given `index` to be equal to `val`.
- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.
- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

**Example 1:**

```

**Input:** ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
**Output:** [null,null,0,null,5]
**Explanation: **
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

**Constraints:**

- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= val <= 10^9`
- `0 <= snap_id < `(the total number of times we call `snap()`)
- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1146 Snapshot Array neetcode](https://www.youtube.com/results?search_query=leetcode+1146+Snapshot+Array+neetcode)

## Approach

### Intuition

Each index changes independently, so store only its value changes and the snapshot ID when each change occurred.

### Brute Force

Copy the whole array at every snapshot and read directly from the chosen copy.

### Optimal

Store sorted snapshot-ID/value pairs per index and binary-search the latest pair at or before the requested snapshot.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | set O(1), snap O(n), get O(1) | O(n * snapshots) |
| Optimal | set O(1), snap O(1), get O(log changes at index) | O(number of set calls) |

### Edge cases

- An index with no prior writes has value zero.
- Several writes before one snap retain only the last value for that snapshot.
