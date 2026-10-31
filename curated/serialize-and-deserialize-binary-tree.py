from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: build level-order input with None entries for absent children.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
    # The index consumes the next left/right slots for each queued parent.
    i = 1
    while q and i < len(values):
        node = q.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# Test helper: serialize level order and trim only redundant trailing None values.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Preorder plus explicit nulls uniquely identifies every binary-tree shape.
        values = []

        def visit(node: Optional[TreeNode]) -> None:
            # Null markers preserve shape, including missing children of skewed trees.
            if node is None:
                values.append("#")
                return
            # Store values before child tokens to establish preorder consumption.
            values.append(str(node.val))
            visit(node.left)
            visit(node.right)

        visit(root)
        # Commas separate tokens; the null marker distinguishes missing children.
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # A shared iterator makes each recursive subtree consume the next token.
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            # Each recursive call consumes exactly one token from the shared iterator.
            value = next(tokens)
            if value == "#":
                return None
            # Consume preorder in the same root-left-right order used by serialize.
            return TreeNode(int(value), build(), build())

        return build()


if __name__ == "__main__":
    codec = Codec()
    for values in ([1, 2, 3, None, None, 4, 5], [], [1], [1, None, 2, None, 3]):
        assert tree_to_list(
            codec.deserialize(codec.serialize(build_tree(list(values))))
        ) == list(values)
    print("All tests passed")
