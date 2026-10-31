# 353. Design Snake Game

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Design, Queue, Simulation  
**Companies:** Atlassian, WeRide, IXL, Salesforce, Uber, Google, Amazon, Bloomberg, Microsoft  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-snake-game/](https://leetcode.com/problems/design-snake-game/)

## Problem

Simulate a snake moving on a bounded grid and eating food in a fixed sequence. Return its current length minus one after each safe move, or -1 when it hits a wall or itself. Example 1: on a 3 by 2 board with food at (1,2) then (0,1), moves R,D,R,U,L,U return 0,0,1,1,2,-1. Example 2: on a 2 by 2 board with food at (0,1) then (1,1), moves R,D return 0,1. Constraints: moves are U, D, L, or R, and the food list is finite.

## Video Explanation

[YouTube search: Search YouTube for leetcode 353 Design Snake Game neetcode](https://www.youtube.com/results?search_query=leetcode+353+Design+Snake+Game+neetcode)

## Approach

### Intuition

Track the body from tail to head and a set of occupied cells for constant-time collision checks.

### Brute Force

Store the body as a list and scan every segment for collisions after each move.

### Optimal

Use a deque for the body and a set of occupied coordinates; temporarily release the tail unless food is eaten.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | move O(length) | O(length + food) |
| Optimal | move O(1) average | O(length + food) |

### Edge cases

- Moving into the current tail cell is safe when the snake is not growing.
- Once game over occurs, later moves continue returning -1.
