"""
LeetCode 1628: Design an Expression Tree With Evaluate Function
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1628+Design+an+Expression+Tree+With+Evaluate+Function+neetcode
Complexity:
    - Time: buildTree O(n), evaluate O(n)
    - Space: O(n) tree plus O(h) evaluation stack
"""

from typing import List, Optional


class Node:
    # Operator nodes own two expression subtrees; leaves store integer tokens.
    # The recursive evaluator preserves the original operand ordering.
    def __init__(
        self, val: str = "", left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.left is None and self.right is None:
            # Operand leaves store their integer directly as text.
            return int(self.val)
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()
        # Recursion evaluates child expressions before applying this operator.
        if self.val == "+":
            return left_value + right_value
        if self.val == "-":
            return left_value - right_value
        if self.val == "*":
            return left_value * right_value
        # Integer arithmetic truncates toward zero without float precision loss.
        quotient = abs(left_value) // abs(right_value)
        return -quotient if (left_value < 0) != (right_value < 0) else quotient


class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> Optional[Node]:
        stack: List[Node] = []
        # A postfix operator always follows both of its operand subtrees.
        for token in postfix:
            if token not in {"+", "-", "*", "/"}:
                stack.append(Node(token))
                continue
            # The second popped node is the operator's right operand.
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
            # The combined subtree becomes one operand for a later operator.
        return stack[-1] if stack else None


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    builder = None
    for op, values in zip(ops, args):
        if op == "TreeBuilder":
            builder = TreeBuilder()
            outputs.append(None)
        else:
            root = getattr(builder, op)(*values)
            outputs.append(root.evaluate() if root else None)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TreeBuilder", "buildTree", "buildTree", "buildTree"],
        [[], [["3", "4", "+", "2", "*"]], [["5", "2", "-"]], [["7"]]],
    ) == [None, 14, 3, 7]
    assert TreeBuilder().buildTree(["0", "3", "-"]).evaluate() == -3
    print("All tests passed")
