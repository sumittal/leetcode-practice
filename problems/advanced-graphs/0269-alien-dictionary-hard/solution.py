"""
LeetCode 269: Alien Dictionary
Difficulty: Hard
Pattern: Advanced Graphs
Video Reference: https://www.youtube.com/watch?v=6kTZYvNNyps
Complexity:
    - Time: O(total chars + V + E)
    - Space: O(V+E)
"""

from collections import deque
from typing import Dict, List, Set


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # graph records successor constraints while indegree counts unsatisfied predecessors.
        characters = set("".join(words))
        graph = {character: set() for character in characters}
        indegree = {character: 0 for character in characters}
        # Include isolated letters so the returned order covers every observed character.
        for first, second in zip(words, words[1:]):
            # Only the first mismatch determines ordering between adjacent words.
            limit = min(len(first), len(second))
            if first[:limit] == second[:limit] and len(first) > len(second):
                return ""
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        # Deduplicate edges so one relation contributes one indegree.
                        graph[a].add(b)
                        indegree[b] += 1
                    break  # Later letters cannot constrain the first differing pair.
        queue = deque(character for character in characters if indegree[character] == 0)
        order = []
        # Kahn's queue emits only characters whose predecessors are already placed.
        while queue:
            char = queue.popleft()
            order.append(char)
            for nxt in graph[char]:
                # A successor is ready only after its final incoming edge is removed.
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        # Unemitted characters mean a precedence cycle makes the alphabet impossible.
        # Emit an order only when every observed character was available to the traversal.
        return "".join(order) if len(order) == len(characters) else ""


def valid_order(words: List[str], order: str) -> bool:
    chars = set("".join(words))
    if set(order) != chars or len(order) != len(chars):
        return False
    rank = {character: i for i, character in enumerate(order)}
    for a, b in zip(words, words[1:]):
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        if i == min(len(a), len(b)):
            if len(a) > len(b):
                return False
        elif rank[a[i]] >= rank[b[i]]:
            return False
    return True


if __name__ == "__main__":
    solution = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    assert valid_order(words, solution.alienOrder(words))
    words = ["z", "x"]
    assert valid_order(words, solution.alienOrder(words))
    ambiguous = ["za", "zb", "ca", "cb"]
    assert valid_order(ambiguous, solution.alienOrder(ambiguous))
    assert solution.alienOrder(["abc", "ab"]) == ""
    assert solution.alienOrder(["z", "x", "z"]) == ""
    print("All tests passed")
