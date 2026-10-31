# 875. Koko Eating Bananas

**Difficulty:** Medium  
**Tags:** Array, Binary Search  
**Companies:** oyo, Trexquant, Nokia, Ripple, Turing, DoorDash, Amazon, Adobe, Accenture, Okta, Swiggy, Expedia, Microsoft, Bloomberg, Oracle (+25 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)

## Problem

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

**Example 1:**

```

**Input:** piles = [3,6,7,11], h = 8
**Output:** 4

```

**Example 2:**

```

**Input:** piles = [30,11,23,4,20], h = 5
**Output:** 30

```

**Example 3:**

```

**Input:** piles = [30,11,23,4,20], h = 6
**Output:** 23

```

**Constraints:**

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Video Explanation

[Koko Eating Bananas - Binary Search - Leetcode 875 - Python](https://www.youtube.com/watch?v=U2SozAs9RzA)

## Approach

### Intuition

Feasibility is monotone: if Koko finishes at speed k, every higher speed also works.

### Brute Force

Try every integer speed from one through the largest pile.

### Optimal

Binary search the answer and sum each pile's ceiling division to test a candidate speed.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n max(piles)) | O(1) |
| Optimal | O(n log(max(piles))) | O(1) |

### Edge cases

- A speed equal to the largest pile handles every pile in at most one hour.
- Ceiling division is needed for piles not divisible by the speed.
