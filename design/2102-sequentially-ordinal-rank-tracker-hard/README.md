# 2102. Sequentially Ordinal Rank Tracker

**Difficulty:** Hard  
**Tags:** Design, Heap (Priority Queue), Data Stream, Ordered Set  
**Companies:** Amazon  
**Pattern:** Design  
**LeetCode:** [https://leetcode.com/problems/sequentially-ordinal-rank-tracker/](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/)

## Problem

A scenic location is represented by its `name` and attractiveness `score`, where `name` is a **unique** string among all locations and `score` is an integer. Locations can be ranked from the best to the worst. The **higher** the score, the better the location. If the scores of two locations are equal, then the location with the **lexicographically smaller** name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

- **Adding** scenic locations, **one at a time**.
- **Querying** the `i^th` **best** location of **all locations already added**, where `i` is the number of times the system has been queried (including the current query).
  - For example, when the system is queried for the `4^th` time, it returns the `4^th` best location of all locations already added.

Note that the test data are generated so that **at any time**, the number of queries **does not exceed** the number of locations added to the system.

Implement the `SORTracker` class:

- `SORTracker()` Initializes the tracker system.
- `void add(string name, int score)` Adds a scenic location with `name` and `score` to the system.
- `string get()` Queries and returns the `i^th` best location, where `i` is the number of times this method has been invoked (including this invocation).

**Example 1:**

```

**Input**
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
**Output**
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

**Explanation**
SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get();              // The sorted locations, from best to worst, are: branford, bradford.
                            // Note that branford precedes bradford due to its **higher score** (3 > 2).
                            // This is the 1^st time get() is called, so return the best location: "branford".
tracker.add("alps", 2);     // Add location with name="alps" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford.
                            // Note that alps precedes bradford even though they have the same score (2).
                            // This is because "alps" is **lexicographically smaller** than "bradford".
                            // Return the 2^nd best location "alps", as it is the 2^nd time get() is called.
tracker.add("orland", 2);   // Add location with name="orland" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford, orland.
                            // Return "bradford", as it is the 3^rd time get() is called.
tracker.add("orlando", 3);  // Add location with name="orlando" and score=3 to the system.
tracker.get();              // Sorted locations: branford, orlando, alps, bradford, orland.
                            // Return "bradford".
tracker.add("alpine", 2);   // Add location with name="alpine" and score=2 to the system.
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "bradford".
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "orland".

```

**Constraints:**

- `name` consists of lowercase English letters, and is unique among all locations.
- `1 <= name.length <= 10`
- `1 <= score <= 10^5`
- At any time, the number of calls to `get` does not exceed the number of calls to `add`.
- At most `4 * 10^4` calls **in total** will be made to `add` and `get`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2102 Sequentially Ordinal Rank Tracker neetcode](https://www.youtube.com/results?search_query=leetcode+2102+Sequentially+Ordinal+Rank+Tracker+neetcode)

## Approach

### Intuition

The i-th query needs the i-th best location among everything added so far, even when new locations arrive between queries.

### Brute Force

Keep all locations and sort them by score descending and name ascending for every get.

### Optimal

Maintain two heaps: the best q queried locations with their worst at the top, and all remaining locations with their best at the top. Rebalance after each add.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add O(1), get O(n log n) | O(n) |
| Optimal | add O(log n), get O(log n) | O(n) |

### Edge cases

- Equal scores rank the lexicographically smaller name first.
- A new location may outrank a previously returned location and must move across the heap boundary.
