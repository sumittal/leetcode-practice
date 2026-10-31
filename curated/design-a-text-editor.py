from typing import List, Optional, Union


class TextEditor:
    def __init__(self):
        # Stack ends are adjacent to the cursor and make local edits efficient.
        self.left: List[str] = []
        self.right: List[str] = []

    def addText(self, text: str) -> None:
        # The left stack is always the text before the cursor.
        self.left.extend(text)
        # Extending the stack appends all new characters immediately before cursor.

    def deleteText(self, k: int) -> int:
        deleted = min(k, len(self.left))
        # Popping removes the nearest characters without rebuilding the text.
        for _ in range(deleted):
            self.left.pop()
        # The return value is the number removed, not the requested k.
        return deleted

    def cursorLeft(self, k: int) -> str:
        # Transferring one character preserves the order around the cursor.
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        # Only the ten-character suffix is materialized for the response.
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            # The right stack's end is the next character after the cursor.
            self.left.append(self.right.pop())
        # All characters remain partitioned between the cursor-side stacks.
        return "".join(self.left[-10:])


def replay(
    ops: List[str], args: List[List[Union[int, str]]]
) -> List[Optional[Union[int, str]]]:
    outputs: List[Optional[Union[int, str]]] = []
    editor = None
    for operation, values in zip(ops, args):
        if operation == "TextEditor":
            editor = TextEditor()
            outputs.append(None)
        else:
            outputs.append(getattr(editor, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TextEditor", "addText", "deleteText", "addText", "cursorRight",
         "cursorLeft", "deleteText", "cursorLeft", "cursorRight"],
        [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]],
    ) == [None, None, 4, None, "etpractice", "leet", 4, "", "practi"]
    assert replay(
        ["TextEditor", "addText", "cursorLeft", "cursorLeft", "cursorRight"],
        [[], ["abc"], [9], [1], [9]],
    ) == [None, None, "", "", "abc"]
    print("All tests passed")
