from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen contains exactly the values encountered earlier in the scan.
        seen = set()
        for value in nums:
            # Check before insertion so the first repeated occurrence is detected.
            if value in seen:
                # The repeated value proves that two array positions are equal.
                return True
            # Remember this first occurrence so a later position can match it.
            seen.add(value)
        # Exhausting the input without a hit means every value was unique.
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) is True
    assert solution.containsDuplicate([1, 2, 3, 4]) is False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert solution.containsDuplicate([]) is False
    assert solution.containsDuplicate([-1, 0, -1]) is True
    print("All tests passed")
