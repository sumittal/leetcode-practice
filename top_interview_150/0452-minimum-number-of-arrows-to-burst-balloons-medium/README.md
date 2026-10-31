# 452. Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium  
**Tags:** Array, Greedy, Sorting  
**Companies:** Expedia, Barclays, Zoho, Microsoft, TikTok, Goldman Sachs, Amazon, Bloomberg, Google  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Problem

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x<sub>start</sub>, x<sub>end</sub>]` denotes a balloon whose **horizontal diameter** stretches between `x<sub>start</sub>` and `x<sub>end</sub>`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `x<sub>start</sub>` and `x<sub>end</sub>` is **burst** by an arrow shot at `x` if `x<sub>start</sub> <= x <= x<sub>end</sub>`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

**Example 1:**

```

**Input:** points = [[10,16],[2,8],[1,6],[7,12]]
**Output:** 2
**Explanation:** The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

```

**Example 2:**

```

**Input:** points = [[1,2],[3,4],[5,6],[7,8]]
**Output:** 4
**Explanation:** One arrow needs to be shot for each balloon for a total of 4 arrows.

```

**Example 3:**

```

**Input:** points = [[1,2],[2,3],[3,4],[4,5]]
**Output:** 2
**Explanation:** The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

```

**Constraints:**

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x<sub>start</sub> < x<sub>end</sub> <= 2^31 - 1`

## Video Explanation

[YouTube search: Search YouTube for leetcode 452 Minimum Number of Arrows to Burst Balloons neetcode](https://www.youtube.com/results?search_query=leetcode+452+Minimum+Number+of+Arrows+to+Burst+Balloons+neetcode)

## Approach

### Intuition

An arrow placed at the earliest ending point of an overlap can burst every balloon in that overlap.

### Brute Force

Try arrow positions at balloon endpoints and count how many balloons each position can burst.

### Optimal

Sort intervals by end coordinate and shoot a new arrow only when the next interval starts after the current arrow.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Optimal | O(n log n) | O(n) |

### Edge cases

- Touching endpoints belong to the same intersection.
- A single balloon needs one arrow.
- An empty interval list needs no arrows.
