# 631. Design Excel Sum Formula

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Array, Hash Table, String, Graph Theory, Design, Topological Sort, Matrix  
**Companies:** Airbnb, Waymo, Rippling, OpenAI, Microsoft, Google, Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-excel-sum-formula/](https://leetcode.com/problems/design-excel-sum-formula/)

## Problem

Create a small spreadsheet whose cells can hold values or formulas that sum referenced cells and rectangular ranges. Example 1: set A1 to 2, then make C3 sum A1 and the range A1:B2; C3 evaluates to 4 because A1 is included twice. Example 2: after setting B2 to 2, the same formula evaluates to 6. Constraints: formulas contain valid cell references and ranges, and formula dependencies contain no cycles.

## Video Explanation

[YouTube search: Search YouTube for leetcode 631 Design Excel Sum Formula neetcode](https://www.youtube.com/results?search_query=leetcode+631+Design+Excel+Sum+Formula+neetcode)

## Approach

### Intuition

Store formulas as counted cell dependencies and evaluate them recursively so later edits to referenced cells are reflected.

### Brute Force

Expand every formula into a fixed value whenever it is assigned, then scan dependent cells after each update.

### Optimal

Store each formula as a multiset of referenced cells and recursively compute the current value when queried.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | set O(1), get O(1), sum O(range area + affected cells) | O(cells + formula references) |
| Optimal | set O(1), get O(dependency graph), sum O(referenced cells + dependency graph) | O(cells + formula references) |

### Edge cases

- Repeated cell references contribute repeatedly to the sum.
- An unset cell has value zero, and setting a formula cell replaces its old formula.
