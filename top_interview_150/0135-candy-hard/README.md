# 135. Candy

**Difficulty:** Hard  
**Tags:** Array, Greedy  
**Companies:** Dropbox, SAP, Bloomberg, Morgan Stanley, Amazon, Walmart Labs, Infosys, Google, Microsoft, Uber, Accenture, Intuit, Visa, Goldman Sachs, TikTok (+2 more)  
**Pattern:** Greedy  
**LeetCode:** [https://leetcode.com/problems/candy/](https://leetcode.com/problems/candy/)

## Problem

There are `n` children standing in a line.

Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have **at least** one candy.
- Children with a **higher** rating get more candies than their neighbors.

Return the **minimum** number of candies you need to have to distribute the candies to the children.

**Example 1:**

```

**Input:** ratings = [1,0,2]
**Output:** 5
**Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

```

**Example 2:**

```

**Input:** ratings = [1,2,2]
**Output:** 4
**Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

```

**Constraints:**

- `1 <= n == ratings.length <= 5 * 10^4`
- `0 <= ratings[i] <= 5 * 10^4`

## Video Explanation

[Candy - Leetcode 135 - Python](https://www.youtube.com/watch?v=1IzCRCcK17A)

## Approach

### Intuition

Every child needs one candy, and each higher-rated neighbor must receive more than the lower-rated neighbor.

### Brute Force

Repeatedly increase candies for any rating violation until no neighbor constraint is broken.

### Optimal

Initialize each child to one, enforce rising slopes left-to-right, then enforce falling slopes right-to-left using the larger required count.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n) |
| Optimal | O(n) | O(n) |

### Edge cases

- A single child receives one candy.
- Equal adjacent ratings impose no ordering constraint.
- The second pass must preserve the larger count established by the first pass.
