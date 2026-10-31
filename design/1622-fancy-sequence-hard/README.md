# 1622. Fancy Sequence

**Difficulty:** Hard  
**Tags:** Math, Design, Segment Tree, Number Theory, Fermat's Little Theorem  
**Companies:** Google, Bloomberg, Amazon  
**Pattern:** Math  
**LeetCode:** [https://leetcode.com/problems/fancy-sequence/](https://leetcode.com/problems/fancy-sequence/)

## Problem

Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations.

Implement the `Fancy` class:

- `Fancy()` Initializes the object with an empty sequence.
- `void append(val)` Appends an integer `val` to the end of the sequence.
- `void addAll(inc)` Increments all existing values in the sequence by an integer `inc`.
- `void multAll(m)` Multiplies all existing values in the sequence by an integer `m`.
- `int getIndex(idx)` Gets the current value at index `idx` (0-indexed) of the sequence **modulo** `10^9 + 7`. If the index is greater or equal than the length of the sequence, return `-1`.

**Example 1:**

```

**Input**
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
**Output**
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

**Explanation**
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

```

**Constraints:**

- `1 <= val, inc, m <= 100`
- `0 <= idx <= 10^5`
- At most `10^5` calls total will be made to `append`, `addAll`, `multAll`, and `getIndex`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1622 Fancy Sequence neetcode](https://www.youtube.com/results?search_query=leetcode+1622+Fancy+Sequence+neetcode)

## Approach

### Intuition

All range-wide operations form one affine transform modulo the prime, so old values can be normalized against it.

### Brute Force

Apply every add and multiply operation to every stored element.

### Optimal

Store values in the inverse of the current multiplier and keep lazy multiplier/addition terms; reset the active epoch on multiplication by zero.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | append O(1), addAll/multAll O(n), getIndex O(1) | O(n) |
| Optimal | append O(log MOD), addAll O(1), multAll O(1), getIndex O(1) | O(n) |

### Edge cases

- Multiplication by zero resets every earlier element to the current affine offset.
- Indices beyond the sequence length return -1.
