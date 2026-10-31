# 68. Text Justification

**Difficulty:** Hard  
**Tags:** Array, String, Simulation  
**Companies:** Visa, Airbnb, Karat, SIG, Sentry, Capital One, Robinhood, Hive, MongoDB, Quora, TikTok, Roblox, Tinder, SoFi, WeRide (+19 more)  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/text-justification/](https://leetcode.com/problems/text-justification/)

## Problem

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
- The input array `words` contains at least one word.

**Example 1:**

```

**Input:** words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
**Output:**
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:**

```

**Input:** words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
**Output:**
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
**Explanation:** Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

**Example 3:**

```

**Input:** words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
**Output:**
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

**Constraints:**

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only English letters and symbols.
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

## Video Explanation

[Text Justification - Leetcode 68 - Python](https://www.youtube.com/watch?v=TzMl4Z7pVh8)

## Approach

### Intuition

Greedily pack the longest prefix of words that fits, then distribute each line's spaces according to whether it is final.

### Brute Force

Try every possible line break and enumerate all whitespace distributions for each line.

### Optimal

Choose maximal word groups, use quotient/remainder to spread spaces evenly, and left-align the final line.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(n) |
| Optimal | O(total characters) | O(total output) |

### Edge cases

- A line with one word receives trailing spaces.
- The final line is left-justified with single spaces between words.
- Extra spaces on a nonfinal line go to its leftmost gaps.
