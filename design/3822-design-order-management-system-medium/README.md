# 3822. Design Order Management System

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Hash Table, Design  
**Companies:** Optiver  
**Pattern:** Hash Table  
**LeetCode:** [https://leetcode.com/problems/design-order-management-system/](https://leetcode.com/problems/design-order-management-system/)

## Problem

Track active buy and sell orders by unique order ID, type, and price. Orders can be added, repriced, canceled, or queried by type and price; the query returns matching active IDs in any order. Example 1: orders 4 and 5 at (buy, 10) are both returned; changing order 4 to price 11 leaves only order 5 in the first query. Example 2: canceling the only order at a key makes that key return an empty list. Constraints: order IDs are globally unique, and modify/cancel target an active order.

## Video Explanation

[YouTube search: Search YouTube for leetcode 3822 Design Order Management System neetcode](https://www.youtube.com/results?search_query=leetcode+3822+Design+Order+Management+System+neetcode)

## Approach

### Intuition

Updates need a direct route from order ID to its current bucket, while queries need direct access to a type-and-price bucket.

### Brute Force

Store all orders by ID and scan active orders for each query.

### Optimal

Maintain an ID-to-order map and a reverse map from (type, price) to a set of IDs.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | add/modify/cancel O(1), getOrdersAtPrice O(n) | O(n) |
| Optimal | add/modify/cancel O(1) expected, query O(k) | O(n) |

### Edge cases

- Changing a price removes the ID from its former bucket before inserting it into the new one.
- An empty bucket is removed after cancellation or repricing.
