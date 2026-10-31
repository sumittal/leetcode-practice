

class _Node:
    def __init__(self) -> None:
        self.children = {}  # type: Dict[str, _Node]
        self.terminal = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = _Node()

    def addWord(self, word: str) -> None:
        node = self.root
        # Every traversed edge represents one character of the inserted word.
        for char in word:
            node = node.children.setdefault(char, _Node())
        # An empty word marks the root terminal, just like any other final node.
        node.terminal = True

    def search(self, word: str) -> bool:
        def match(node: _Node, index: int) -> bool:
            # The recursive contract is whether this suffix matches below node.
            # Pattern exhaustion is valid only when this trie node ends a word.
            if index == len(word):
                return node.terminal
            char = word[index]
            if char != ".":
                # Literal positions follow exactly one trie edge.
                return char in node.children and match(node.children[char], index + 1)
            # A dot consumes one character, so try each child at only this depth.
            # Each recursive branch advances one position, preventing wildcard reuse.
            return any(match(child, index + 1) for child in node.children.values())

        return match(self.root, 0)


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    for word in ("bad", "dad", "mad"):
        word_dictionary.addWord(word)
    assert [word_dictionary.search(x) for x in ("pad", "bad", ".ad", "b..")] == [
        False,
        True,
        True,
        True,
    ]
    assert word_dictionary.search("..") is False
    assert word_dictionary.search("...") is True
    print("All tests passed")
