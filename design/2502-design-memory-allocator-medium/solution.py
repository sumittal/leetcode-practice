"""
LeetCode 2502: Design Memory Allocator
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+2502+Design+Memory+Allocator+neetcode
Complexity:
    - Time: allocate O(n), freeMemory O(n)
    - Space: O(n)
"""

from typing import List, Optional


class Allocator:
    # Linear first-fit scans trade O(n) search for constant per-cell storage.
    def __init__(self, n: int):
        # Zero denotes a free memory unit; positive IDs denote its owner.
        self.memory: List[int] = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        # A running free-run length identifies the earliest adequate block.
        run_start = 0
        run_length = 0
        for index, owner in enumerate(self.memory):
            if owner == 0:
                if run_length == 0:
                    run_start = index
                run_length += 1
                if run_length == size:
                    # The first complete run is the required leftmost fit.
                    for allocated in range(run_start, run_start + size):
                        self.memory[allocated] = mID
                    # Mark the whole block before returning its first address.
                    return run_start
            else:
                # An occupied cell breaks the candidate free interval.
                run_length = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        # An ID can own several separated blocks, so scan all cells.
        freed = 0
        for index, owner in enumerate(self.memory):
            if owner == mID:
                self.memory[index] = 0
                freed += 1
        # A full scan handles disjoint allocations that share the same ID.
        return freed


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    allocator = None
    for operation, values in zip(ops, args):
        if operation == "Allocator":
            allocator = Allocator(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(allocator, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Allocator", "allocate", "allocate", "allocate", "freeMemory",
         "allocate", "allocate", "allocate", "freeMemory", "allocate",
         "freeMemory"],
        [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1],
         [1], [10, 2], [7]],
    ) == [None, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]
    assert replay(
        ["Allocator", "allocate", "freeMemory", "allocate"],
        [[3], [4, 9], [9], [3, 8]],
    ) == [None, -1, 0, 0]
    print("All tests passed")
