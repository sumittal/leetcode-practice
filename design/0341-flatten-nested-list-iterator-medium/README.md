# 341. Flatten Nested List Iterator

**Difficulty:** Medium  
**Tags:** Stack, Tree, Depth-First Search, Design, Queue, Iterator  
**Companies:** Mixpanel, X, OpenAI, Warnermedia, Adobe, Aurora, Yahoo, Apple, LinkedIn, Tesla, Walmart Labs, Meta, DE Shaw, Google, Amazon (+2 more)  
**Pattern:** Stack  
**LeetCode:** [https://leetcode.com/problems/flatten-nested-list-iterator/](https://leetcode.com/problems/flatten-nested-list-iterator/)

## Problem

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

- `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
- `int next()` Returns the next integer in the nested list.
- `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:

```

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

```

If `res` matches the expected flattened list, then your code will be judged as correct.

**Example 1:**

```

**Input:** nestedList = [[1,1],2,[1,1]]
**Output:** [1,1,2,1,1]
**Explanation:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

```

**Example 2:**

```

**Input:** nestedList = [1,[4,[6]]]
**Output:** [1,4,6]
**Explanation:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

```

**Constraints:**

- `1 <= nestedList.length <= 500`
- The values of the integers in the nested list is in the range `[-10^6, 10^6]`.

## Video Explanation

[YouTube search: Search YouTube for leetcode 341 Flatten Nested List Iterator neetcode](https://www.youtube.com/results?search_query=leetcode+341+Flatten+Nested+List+Iterator+neetcode)

## Approach

### Intuition

Keep iterators for the current nesting levels and descend only when the next item is a list.

### Brute Force

Recursively flatten the entire input into a second list before iteration.

### Optimal

Use a stack of list iterators and expand nested lists lazily until an integer is ready.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), next O(1), hasNext O(1) | O(n) |
| Optimal | next O(1) amortized, hasNext O(depth) amortized | O(depth) |

### Edge cases

- Nested lists may contain other lists several levels deep.
- An empty nested list contributes no values.
