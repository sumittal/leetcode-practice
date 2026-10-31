# 1261. Find Elements in a Contaminated Binary Tree

**Difficulty:** Medium  
**Tags:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree  
**Companies:** Google, Amazon  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/)

## Problem

Given a binary tree with the following rules:

1. `root.val == 0`
2. For any `treeNode`:
  1. If `treeNode.val` has a value `x` and `treeNode.left != null`, then `treeNode.left.val == 2 * x + 1`
  2. If `treeNode.val` has a value `x` and `treeNode.right != null`, then `treeNode.right.val == 2 * x + 2`

Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.

Implement the `FindElements` class:

- `FindElements(TreeNode* root)` Initializes the object with a contaminated binary tree and recovers it.
- `bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg)

```

**Input**
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
**Output**
[null,false,true]
**Explanation**
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg)

```

**Input**
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
**Output**
[null,true,true,false]
**Explanation**
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg)

```

**Input**
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
**Output**
[null,true,false,false,true]
**Explanation**
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

```

**Constraints:**

- `TreeNode.val == -1`
- The height of the binary tree is less than or equal to `20`
- The total number of nodes is between `[1, 10^4]`
- Total calls of `find()` is between `[1, 10^4]`
- `0 <= target <= 10^6`

## Video Explanation

[YouTube search: Search YouTube for leetcode 1261 Find Elements in a Contaminated Binary Tree neetcode](https://www.youtube.com/results?search_query=leetcode+1261+Find+Elements+in+a+Contaminated+Binary+Tree+neetcode)

## Approach

### Intuition

Recovered values follow a deterministic rule from each node's parent value.

### Brute Force

Recover the whole tree and search it from the root for every target.

### Optimal

Recover all values once into a set and use constant-time membership checks.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | construction O(n), find O(n) | O(n) |
| Optimal | construction O(n), find O(1) expected | O(n) |

### Edge cases

- The root is recovered as value zero.
- A target absent from the tree returns false.
