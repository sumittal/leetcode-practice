# 621. Task Scheduler

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting  
**Pattern:** Heap / Priority Queue  
**LeetCode:** [https://leetcode.com/problems/task-scheduler/](https://leetcode.com/problems/task-scheduler/)

## Problem

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

**Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2

**Output:** 8

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.

**Example 2:**

**Input:** tasks = ["A","C","A","B","D","B"], n = 1

**Output:** 6

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

**Example 3:**

**Input:** tasks = ["A","A","A", "B","B","B"], n = 3

**Output:** 10

**Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

**Constraints:**

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Video Explanation

[Task Scheduler - Leetcode 621 - Python](https://www.youtube.com/watch?v=s8p8ukTyA2I)

## Approach

### Intuition

The most frequent task determines a lower bound, with other tasks filling available cooldown slots.

### Brute Force

Simulate each time unit by selecting an available task with the greatest remaining count.

### Optimal

Count the maximum frequency and how many tasks share it, then take the larger of total tasks and the frame length imposed by that maximum.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(T log A) | O(A) |
| Optimal | O(T + A) | O(A) |

### Edge cases

- A zero cooldown means no idle slots are needed.
- Several tasks may tie for the maximum frequency.
