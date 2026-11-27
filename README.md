# LeetCode Practice

A locally generated study repo with problem statements, curated approaches, and runnable Python solutions.

## Browse by topic or difficulty

Choose a topic from the first column or a difficulty from the header.

| Topic | [Easy](by_difficulty/easy.md) | [Medium](by_difficulty/medium.md) | [Hard](by_difficulty/hard.md) | Total |
| --- | ---: | ---: | ---: | ---: |
| [1-D Dynamic Programming](problems/1-d-dynamic-programming/README.md) | 2 | 11 | 0 | 13 |
| [2-D Dynamic Programming](problems/2-d-dynamic-programming/README.md) | 0 | 10 | 4 | 14 |
| [Advanced Graphs](problems/advanced-graphs/README.md) | 0 | 3 | 3 | 6 |
| [Arrays & Hashing](problems/arrays-and-hashing/README.md) | 23 | 79 | 16 | 118 |
| [Backtracking](problems/backtracking/README.md) | 0 | 9 | 2 | 11 |
| [Binary Search](problems/binary-search/README.md) | 3 | 8 | 4 | 15 |
| [Bit Manipulation](problems/bit-manipulation/README.md) | 6 | 3 | 0 | 9 |
| [Depth-First Search](problems/depth-first-search/README.md) | 0 | 0 | 1 | 1 |
| [Design](problems/design/README.md) | 1 | 2 | 4 | 7 |
| [Graphs](problems/graphs/README.md) | 0 | 14 | 2 | 16 |
| [Greedy](problems/greedy/README.md) | 0 | 9 | 1 | 10 |
| [Heap / Priority Queue](problems/heap-priority-queue/README.md) | 2 | 5 | 2 | 9 |
| [Intervals](problems/intervals/README.md) | 1 | 4 | 2 | 7 |
| [Linked List](problems/linked-list/README.md) | 3 | 16 | 6 | 25 |
| [Math & Geometry](problems/math-and-geometry/README.md) | 4 | 9 | 3 | 16 |
| [Sliding Window](problems/sliding-window/README.md) | 2 | 4 | 2 | 8 |
| [Stack](problems/stack/README.md) | 3 | 9 | 2 | 14 |
| [String](problems/string/README.md) | 0 | 2 | 1 | 3 |
| [Trees](problems/trees/README.md) | 11 | 15 | 3 | 29 |
| [Tries](problems/tries/README.md) | 0 | 2 | 1 | 3 |
| [Two Pointers](problems/two-pointers/README.md) | 3 | 6 | 1 | 10 |
| **Total** | **64** | **220** | **60** | **344** |

## Overall progress

- Easy: 64/64 solved
- Medium: 220/220 solved
- Hard: 60/60 solved

## Usage

Problems live in `problems/<topic>/<id>-<slug>-<difficulty>/`. Placement uses the problem's
`Pattern` (curated pattern, then NeetCode pattern, then the first LeetCode tag). Related
patterns such as Array and Hash Table share a topic. Untagged problems use Not specified.

The **Study list** column keeps the original, non-overlapping list grouping:
Blind 75, the remaining NeetCode 150 problems, then additional Top Interview 150 and
LeetCode Design problems. The list is not an exhaustive set of overlapping memberships.

Fetch a list or selected problems to generate their files and update the indexes.
Use `--index-only` to run solution self-checks and rebuild all indexes offline from local files.

```sh
python3 fetch_problems.py --list neetcode150
python3 fetch_problems.py --list neetcode150-extra --start 0 --batch-size 25
python3 fetch_problems.py --list topinterview150
python3 fetch_problems.py --list topinterview150-extra --start 0 --batch-size 50
python3 fetch_problems.py --list design
python3 fetch_problems.py --list design-extra --start 0 --batch-size 50
python3 fetch_problems.py --list blind75 --start 0 --batch-size 20
python3 fetch_problems.py --slugs two-sum,valid-anagram
python3 fetch_problems.py --index-only
```

Company tags: community-reported data from [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems), ranked by frequency.

## System Design

Read the interview-oriented [system design notes](./system_design/README.md).
