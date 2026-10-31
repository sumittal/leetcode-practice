# 1166. Design File System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, String, Design, Trie  
**Companies:** DoorDash, Airbnb, Coinbase, Snowflake, Capital One, Uber, Amazon, Google, Meta, Microsoft  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-file-system/](https://leetcode.com/problems/design-file-system/)

## Problem

Create paths with integer values and retrieve values only for paths that have been created. A new path is valid only when its immediate parent already exists. Example 1: create /a with value 1, then /a/b with value 2; both values can be read. Example 2: attempting /c/d before /c exists fails, then creating /c allows it to be read. Constraints: paths begin with /, contain lowercase components, and are not the root path.

## Video Explanation

[YouTube search: Search YouTube for leetcode 1166 Design File System neetcode](https://www.youtube.com/results?search_query=leetcode+1166+Design+File+System+neetcode)

## Approach

### Intuition

A path trie lets each creation verify that its parent node exists before inserting the final component.

### Brute Force

Store full path strings and check for a parent path in a set before each insertion.

### Optimal

Store each path component in a trie, locating the parent and final node in one traversal.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | createPath O(path length), get O(1) average | O(number of paths) |
| Optimal | createPath O(path length), get O(path length) | O(total path components) |

### Edge cases

- A path cannot be created twice.
- A child cannot be created before its direct parent.
