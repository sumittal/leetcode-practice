# 2671. Frequency Tracker

**Difficulty:** Medium  
**Tags:** Hash Table, Design  
**Companies:** None reported  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/frequency-tracker/](https://leetcode.com/problems/frequency-tracker/)

## Problem

Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the `FrequencyTracker` class.

- `FrequencyTracker()`: Initializes the `FrequencyTracker` object with an empty array initially.
- `void add(int number)`: Adds `number` to the data structure.
- `void deleteOne(int number)`: Deletes **one** occurrence of `number` from the data structure. The data structure **may not contain** `number`, and in this case nothing is deleted.
- `bool hasFrequency(int frequency)`: Returns `true` if there is a number in the data structure that occurs `frequency` number of times, otherwise, it returns `false`.

**Example 1:**

```

**Input**
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
**Output**
[null, null, null, true]

**Explanation**
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.add(3); // The data structure now contains [3, 3]
frequencyTracker.hasFrequency(2); // Returns true, because 3 occurs twice

```

**Example 2:**

```

**Input**
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
**Output**
[null, null, null, false]

**Explanation**
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // The data structure now contains [1]
frequencyTracker.deleteOne(1); // The data structure becomes empty []
frequencyTracker.hasFrequency(1); // Returns false, because the data structure is empty

```

**Example 3:**

```

**Input**
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
**Output**
[null, false, null, true]

**Explanation**
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // Returns false, because the data structure is empty
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.hasFrequency(1); // Returns true, because 3 occurs once

```

**Constraints:**

- `1 <= number <= 10^5`
- `1 <= frequency <= 10^5`
- At most, `2 * 10^5` calls will be made to `add`, `deleteOne`, and `hasFrequency` in **total**.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2671 Frequency Tracker neetcode](https://www.youtube.com/results?search_query=leetcode+2671+Frequency+Tracker+neetcode)

## Approach

### Intuition

Queries ask whether any number occupies a frequency, so track how many distinct numbers have each frequency.

### Brute Force

Store all values and count each value's occurrences for every query.

### Optimal

Maintain number-to-frequency and frequency-to-number-count maps, updating both on each change.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add/deleteOne O(1), hasFrequency O(n) | O(n) |
| Optimal | add/deleteOne/hasFrequency O(1) expected | O(d + f) |

### Edge cases

- Deleting a missing number has no effect.
- A number leaving a frequency bucket decrements that bucket's distinct-number count.
