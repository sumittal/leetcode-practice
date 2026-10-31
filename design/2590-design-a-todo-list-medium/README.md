# 2590. Design a Todo List

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Hash Table, String, Design, Sorting  
**Companies:** Bloomberg  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/design-a-todo-list/](https://leetcode.com/problems/design-a-todo-list/)

## Problem

Maintain users' tasks with sequential global IDs, due dates, descriptions, tags, and completion state. Queries return only pending descriptions in due-date order, optionally filtered by a tag. Example 1: a user's tasks due on days 4 and 2 are returned in the order of day 2 then day 4. Example 2: completing a task removes it from both task queries, but does not affect another user's task. Constraints: IDs are sequential, due dates are unique, and completion applies only to a task owned by that user.

## Video Explanation

[YouTube search: Search YouTube for leetcode 2590 Design a Todo List neetcode](https://www.youtube.com/results?search_query=leetcode+2590+Design+a+Todo+List+neetcode)

## Approach

### Intuition

Each user's active task records can be filtered and sorted by the unique due date.

### Brute Force

Keep all records in one list and scan every task for each user's query.

### Optimal

Map each user to task records and use a global increasing task ID; sort only that user's matching active tasks for a query.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | addTask O(1), completeTask O(n), query O(n log n) | O(n) |
| Optimal | addTask O(1), completeTask O(1) expected, query O(t log t) | O(n) |

### Edge cases

- Completing a missing task or another user's task has no effect.
- Completed tasks never appear in tag-filtered or unfiltered results.
