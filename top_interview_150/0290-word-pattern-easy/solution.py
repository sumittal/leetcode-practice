"""
LeetCode 290: Word Pattern
Difficulty: Easy
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=W_akoecmCbM
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # The sentence's whitespace is normalized into a word sequence.
        words = s.split()
        if len(pattern) != len(words):
            return False
        # Both maps ensure neither side of the correspondence is reused.
        # Empty maps are consistent before the first aligned pair.
        letter_to_word = {}
        word_to_letter = {}
        # Aligned iteration validates one pattern position at a time.
        for letter, word in zip(pattern, words):
            # A repeated pattern symbol must retain its original word.
            if letter in letter_to_word and letter_to_word[letter] != word:
                return False
            # A word cannot represent two distinct pattern symbols.
            if word in word_to_letter and word_to_letter[word] != letter:
                return False
            letter_to_word[letter] = word
            word_to_letter[word] = letter
            # Updating both directions preserves a bijection prefix by prefix.
            # A later position can reject a conflict in either mapping direction.
        # Equal lengths plus consistent mappings validate every pair.
        # Empty pattern and sentence satisfy the same mapping condition.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordPattern("abba", "dog cat cat dog") is True
    assert solution.wordPattern("abba", "dog cat cat fish") is False
    assert solution.wordPattern("aaaa", "dog cat cat dog") is False
    assert solution.wordPattern("abba", "dog dog dog dog") is False
    print("All tests passed")
