# 6. Zigzag Conversion

**Difficulty:** Medium  
**Tags:** String  
**Companies:** PayPal, Zopsmart, Zoho, PayPay, Siemens, Walmart Labs, Bloomberg, Amazon, Oracle, Google, Microsoft, Salesforce, Meta, Infosys, tcs (+1 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/zigzag-conversion/](https://leetcode.com/problems/zigzag-conversion/)

## Problem

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```

P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```

string convert(string s, int numRows);

```

**Example 1:**

```

**Input:** s = "PAYPALISHIRING", numRows = 3
**Output:** "PAHNAPLSIIGYIR"

```

**Example 2:**

```

**Input:** s = "PAYPALISHIRING", numRows = 4
**Output:** "PINALSIGYAHRPI"
**Explanation:**
P     I    N
A   L S  I G
Y A   H R
P     I

```

**Example 3:**

```

**Input:** s = "A", numRows = 1
**Output:** "A"

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

## Video Explanation

[ZigZag Conversion - Leetcode 6 - Python](https://www.youtube.com/watch?v=Q2Tw6gcVEwc)

## Approach

### Intuition

The zigzag path moves down through the rows, then diagonally upward, repeating that cycle.

### Brute Force

Place characters into a full two-dimensional grid and read the rows.

### Optimal

Append each character directly to its current row while reversing direction at the top and bottom.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n * numRows) | O(n * numRows) |
| Optimal | O(n) | O(n) |

### Edge cases

- One row produces the original string.
- More rows than characters also leaves the input order unchanged.
- The direction changes at both boundary rows.
