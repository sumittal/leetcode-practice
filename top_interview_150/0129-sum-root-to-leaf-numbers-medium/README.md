# 129. Sum Root to Leaf Numbers

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Tree  
**Companies:** Meta, Visa, Oracle, tcs, Amazon, Google, Bloomberg, Microsoft  
**Pattern:** Trees  
**LeetCode:** [https://leetcode.com/problems/sum-root-to-leaf-numbers/](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

## Problem

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

```

**Input:** root = [1,2,3]
**Output:** 25
**Explanation:**
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

```

**Input:** root = [4,9,0,5,1]
**Output:** 1026
**Explanation:**
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`.

## Video Explanation

[Sum Root to Leaf Numbers - Coding Interview Question - Leetcode 129](https://www.youtube.com/watch?v=Jk16lZGFWxE)

## Approach

### Intuition

Each root-to-leaf number is formed by appending each node digit to the prefix accumulated from its ancestors.

### Brute Force

Build a string for every root-to-leaf path and convert each string to an integer.

### Optimal

Carry the numeric prefix down the tree using prefix * 10 + node.val, and add it at each leaf.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(nh) | O(nh) |
| Optimal | O(n) | O(h) |

### Edge cases

- A single-node tree contributes that digit.
- Only complete root-to-leaf paths count.
- The input values are decimal digits.
