from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            # There is no first choice from which to form a nonempty combination.
            return []
        letters: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        current = []

        def build(index: int) -> None:
            # A complete path has selected one mapped letter for every digit.
            if index == len(digits):
                result.append("".join(current))
                return
            # The digit index advances exactly once for every chosen character.
            # Each branch fixes this digit before recursing to the next one.
            for letter in letters[digits[index]]:
                current.append(letter)
                build(index + 1)
                current.pop()  # Undo this letter before trying another mapping.
            # Returning restores the prefix belonging to the parent digit.

        # Any full combination uses exactly one branch for each input digit.
        # The output contains the Cartesian product of all per-digit letter choices.
        build(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.letterCombinations("23")) == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert sorted(solution.letterCombinations("2")) == ["a", "b", "c"]
    assert solution.letterCombinations("") == []
    assert sorted(solution.letterCombinations("79")) == sorted(
        [
            "pw",
            "px",
            "py",
            "pz",
            "qw",
            "qx",
            "qy",
            "qz",
            "rw",
            "rx",
            "ry",
            "rz",
            "sw",
            "sx",
            "sy",
            "sz",
        ]
    )
    print("All tests passed")
