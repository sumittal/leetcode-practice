from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(left: int, right: int) -> bool:
            # Compare inward; any unequal pair disproves this substring.
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            # Meeting indices have no remaining pair to invalidate the palindrome.
            return True

        def build(start: int) -> None:
            # Reaching the string end means every chosen piece was a palindrome.
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start, len(s)):
                # Non-palindromic prefixes cannot begin a valid partition branch.
                if not is_palindrome(start, end):
                    continue
                current.append(s[start : end + 1])
                # The next call partitions only the suffix after this chosen piece.
                build(end + 1)
                current.pop()  # Undo the piece before checking a longer prefix.
            # Each call returns with its input prefix restored for its parent.

        # Empty input reaches the base case and yields one empty partition.
        build(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.partition("aab"))) == [
        ("a", "a", "b"),
        ("aa", "b"),
    ]
    assert solution.partition("a") == [["a"]]
    assert solution.partition("") == [[]]
    assert sorted(map(tuple, solution.partition("efe"))) == [
        ("e", "f", "e"),
        ("efe",),
    ]
    print("All tests passed")
