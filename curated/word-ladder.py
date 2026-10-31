from collections import deque
from typing import Dict, List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            # The destination must be a legal dictionary word to finish a sequence.
            return 0
        # Wildcard buckets index words that differ at one position.
        patterns: Dict[str, List[str]] = {}
        words = set(wordList)
        words.add(beginWord)
        # Every word contributes one pattern per character position.
        for word in words:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index + 1 :]
                patterns.setdefault(pattern, []).append(word)
        # BFS layers correspond to transformation sequence lengths.
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        # Marking beginWord prevents a cycle from putting it back in the queue.
        while queue:
            word, sequence_length = queue.popleft()
            if word == endWord:
                # First discovery at the queue front is a shortest transformation.
                return sequence_length
            # Processing every position enumerates all one-letter mutations.
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index + 1 :]
                # All words in this bucket are one legal letter change away.
                neighbors = patterns.get(pattern, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        # Mark at enqueue time so multiple paths cannot duplicate work.
                        visited.add(neighbor)
                        queue.append((neighbor, sequence_length + 1))
                # Every neighbor in a processed bucket was enqueued at its first use.
                # Clearing is safe because the whole bucket was examined in this visit.
                patterns[pattern] = []
            # Emptying buckets prevents repeated scans of the same transformation edges.
        # Exhausting reachable words means no allowed sequence reaches endWord.
        return 0


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        == 5
    )
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert solution.ladderLength("a", "c", ["a", "b", "c"]) == 2
    assert solution.ladderLength("hit", "hit", ["hot"]) == 0
    print("All tests passed")
