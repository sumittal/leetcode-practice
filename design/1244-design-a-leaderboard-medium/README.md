# 1244. Design A Leaderboard

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, Design, Sorting  
**Companies:** Wayfair, Pinterest, Bloomberg, Citadel, DE Shaw, Uber, Google, Amazon  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-a-leaderboard/](https://leetcode.com/problems/design-a-leaderboard/)

## Problem

Maintain player scores as they change, return the sum of the highest k scores, and remove a player's score on reset. Example 1: scores 73, 56, 39, 51, and 4 yield a top-one sum of 73. Example 2: after resetting the 73- and 56-point players and adding 51 points for one of them, the top three sum to 141. Constraints: player IDs are unique while active and requested top counts do not exceed the number of active players.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1244 Design A Leaderboard neetcode](https://www.youtube.com/results?search_query=leetcode+1244+Design+A+Leaderboard+neetcode)

## Approach

### Intuition

A score map supports updates and resets, while sorting active scores answers top-k queries.

### Brute Force

Store scores in a map and sort every score whenever top(k) is requested.

### Optimal

Keep a score map and use a balanced ordered multiset to retrieve the largest k values.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | addScore O(1), top O(n log n), reset O(1) | O(n) |
| Optimal | addScore O(log n), top O(k), reset O(log n) | O(n) |

### Edge cases

- Adding points to an existing player changes rather than replaces the score.
- Resetting a player removes that player's complete score.
