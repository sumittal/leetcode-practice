# 1628. Design an Expression Tree With Evaluate Function

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Math, Stack, Tree, Design, Binary Tree  
**Companies:** Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/)

## Problem

Build an expression tree from postfix tokens and evaluate its arithmetic operators. Example 1: postfix [3, 4, +, 2, *] builds a tree evaluating to 14. Example 2: [5, 2, -] evaluates to 3. Constraints: tokens form a valid expression, operators are +, -, *, or /, and division truncates toward zero.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1628 Design an Expression Tree With Evaluate Function neetcode](https://www.youtube.com/results?search_query=leetcode+1628+Design+an+Expression+Tree+With+Evaluate+Function+neetcode)

## Approach

### Intuition

Postfix operands are ready before their operator, so a stack can assemble each operator node.

### Brute Force

Parse and evaluate postfix tokens directly whenever the expression is requested.

### Optimal

Build the tree in one stack pass and evaluate recursively from its root.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | build/evaluate O(n) | O(n) |
| Optimal | buildTree O(n), evaluate O(n) | O(n) tree plus O(h) evaluation stack |

### Edge cases

- A one-token expression is a leaf node.
- Subtraction and division preserve left/right operand order.
