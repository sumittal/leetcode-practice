"""
LeetCode 1600: Throne Inheritance
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+1600+Throne+Inheritance+neetcode
Complexity:
    - Time: birth/death O(1), getInheritanceOrder O(n)
    - Space: O(n)
"""

from typing import Dict, List, Set


class ThroneInheritance:
    # The family tree is immutable except for ordered births and death markers.
    # A preorder walk naturally follows the required succession order.
    def __init__(self, kingName: str):
        # Child lists preserve birth order for the preorder inheritance walk.
        self.king = kingName
        self.children: Dict[str, List[str]] = {kingName: []}
        self.dead: Set[str] = set()

    def birth(self, parentName: str, childName: str) -> None:
        # Appending preserves the required birth order among siblings.
        self.children.setdefault(parentName, []).append(childName)
        # Every new person starts with an empty ordered child list.
        self.children[childName] = []

    def death(self, name: str) -> None:
        # Death affects whether a person is listed, not their descendants.
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order: List[str] = []
        stack = [self.king]
        while stack:
            person = stack.pop()
            # Dead people are skipped but their descendants are still explored.
            if person not in self.dead:
                order.append(person)
            # Reverse push order makes the stack visit children oldest-first.
            stack.extend(reversed(self.children[person]))
        return order


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    family = None
    for op, values in zip(ops, args):
        if op == "ThroneInheritance":
            family = ThroneInheritance(*values)
            outputs.append(None)
        else:
            result = getattr(family, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ThroneInheritance", "birth", "birth", "birth", "birth", "birth",
         "getInheritanceOrder", "death", "getInheritanceOrder"],
        [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"],
         ["andy", "matthew"], ["bob", "alex"], [], ["bob"], []],
    ) == [None, None, None, None, None, None,
          ["king", "andy", "matthew", "bob", "alex", "catherine"], None,
          ["king", "andy", "matthew", "alex", "catherine"]]
    print("All tests passed")
