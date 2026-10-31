"""
LeetCode 588: Design In-Memory File System
Difficulty: Hard
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+588+Design+In-Memory+File+System+neetcode
Complexity:
    - Time: ls O(c log c), mkdir O(path length), addContentToFile O(path length + content length), readContentFromFile O(path length)
    - Space: O(total path and file content)
"""

from typing import Dict, List, Optional, Union


class FileNode:
    def __init__(self):
        # Direct children make path descent proportional to path depth.
        self.children: Dict[str, "FileNode"] = {}
        # Files and directories share nodes; only files hold appended content.
        self.is_file = False
        self.content = ""


class FileSystem:
    def __init__(self):
        self.root = FileNode()

    def _walk(self, path: str, create: bool = False) -> FileNode:
        # A single traversal handles both directory paths and final file paths.
        node = self.root
        for part in path.split("/")[1:]:
            if not part:
                continue
            if part not in node.children:
                if not create:
                    return FileNode()
                # Missing path components are directories unless a file is final.
                node.children[part] = FileNode()
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._walk(path)
        if node.is_file:
            return [path.rstrip("/").rsplit("/", 1)[-1]]
        # Sorted child names are the required directory listing order.
        return sorted(node.children)

    def mkdir(self, path: str) -> None:
        # Creating an existing directory is harmless in this interface.
        self._walk(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath, create=True)
        node.is_file = True
        # Appends preserve content written in earlier calls.
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        # File content is stored at its terminal trie node.
        return self._walk(filePath).content


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[List[str], str]]]:
    outputs: List[Optional[Union[List[str], str]]] = []
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
        ["FileSystem", "ls", "mkdir", "addContentToFile", "ls",
         "readContentFromFile"],
        [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/a/b"],
         ["/a/b/c/d"]],
    ) == [None, [], None, None, ["c"], "hello"]
    assert replay(
        ["FileSystem", "addContentToFile", "addContentToFile",
         "readContentFromFile", "ls"],
        [[], ["/file", "hello"], ["/file", " world"], ["/file"], ["/file"]],
    ) == [None, None, None, "hello world", ["file"]]
    print("All tests passed")
