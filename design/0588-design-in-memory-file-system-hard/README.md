# 588. Design In-Memory File System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Hard  
**Tags:** Hash Table, String, Design, Trie, Sorting  
**Companies:** Baidu, Netskope, Snowflake, Coinbase, Coupang, DoorDash, Uber, Citadel, Oracle, TikTok, Amazon, Microsoft, Google  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-in-memory-file-system/](https://leetcode.com/problems/design-in-memory-file-system/)

## Problem

Implement a hierarchical file system with directory creation, sorted directory listings, file appends, and file reads. Example 1: create /a/b, add "hello" to /a/b/file, then read that file and receive "hello". Example 2: add " world" to the same file and read "hello world"; listing /a returns ["b"]. Constraints: paths are absolute, components are nonempty, and file operations target valid paths.

## Video Explanation

[YouTube search: Search YouTube for leetcode 588 Design In-Memory File System neetcode](https://www.youtube.com/results?search_query=leetcode+588+Design+In-Memory+File+System+neetcode)

## Approach

### Intuition

A trie naturally represents path components and lets files and directories share their common prefixes.

### Brute Force

Store full path strings and scan them to find each directory's immediate children.

### Optimal

Store child nodes in a trie; each file node owns its content and each directory node owns named children.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | ls O(n), mkdir O(path length), addContentToFile O(path length + content length), readContentFromFile O(1) | O(total path and file content) |
| Optimal | ls O(c log c), mkdir O(path length), addContentToFile O(path length + content length), readContentFromFile O(path length) | O(total path and file content) |

### Edge cases

- Listing a file returns only its basename.
- Appending to an existing file preserves its earlier contents.
