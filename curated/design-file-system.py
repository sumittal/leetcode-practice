from typing import Dict, List, Optional, Union


class PathNode:
    def __init__(self):
        # Child names form a trie path from the root to each created entry.
        self.children: Dict[str, "PathNode"] = {}
        # -1 is reserved for the root and all paths that do not exist.
        self.value = -1


class FileSystem:
    # Trie nodes distinguish a missing path from a created path with value zero.
    def __init__(self):
        # Root exists from construction, allowing one-component paths immediately.
        self.root = PathNode()

    def _parts(self, path: str) -> List[str]:
        # Empty components from the leading slash are not trie nodes.
        return [part for part in path.split("/") if part]

    def createPath(self, path: str, value: int) -> bool:
        parts = self._parts(path)
        node = self.root
        for part in parts[:-1]:
            if part not in node.children:
                # A missing intermediate component means the parent is absent.
                return False
            node = node.children[part]
        if not parts or parts[-1] in node.children:
            return False
        child = PathNode()
        child.value = value
        node.children[parts[-1]] = child
        # Only a newly inserted final node receives the requested value.
        return True

    def get(self, path: str) -> int:
        node = self.root
        for part in self._parts(path):
            if part not in node.children:
                return -1
            node = node.children[part]
        # The root has no created path value and remains distinguishable.
        return node.value


def replay(
    ops: List[str], args: List[List[Union[str, int]]]
) -> List[Optional[Union[int, bool]]]:
    outputs: List[Optional[Union[int, bool]]] = []
    file_system = None
    for operation, values in zip(ops, args):
        if operation == "FileSystem":
            file_system = FileSystem()
            outputs.append(None)
        else:
            outputs.append(getattr(file_system, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FileSystem", "createPath", "get", "createPath", "createPath",
         "get", "createPath", "get"],
        [[], ["/a", 1], ["/a"], ["/a/b", 2], ["/c/d", 1], ["/c/d"],
         ["/c", 1], ["/c"]],
    ) == [None, True, 1, True, False, -1, True, 1]
    assert replay(
        ["FileSystem", "createPath", "createPath", "get", "createPath"],
        [[], ["/leet", 1], ["/leet/code", 2], ["/leet/code"], ["/leet", 3]],
    ) == [None, True, True, 2, False]
    print("All tests passed")
