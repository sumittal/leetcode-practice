from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Empty input has no valid segment endpoints to reverse.
        if not nums:
            return
        # Rotating by a full length returns to the original arrangement.
        k %= len(nums)
        # A zero remainder preserves the array without unnecessary swaps.
        if not k:
            return

        def reverse(left: int, right: int) -> None:
            # Swaps move both endpoints inward until this segment is reversed.
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Whole-array reversal puts the original suffix in reversed front order.
        reverse(0, len(nums) - 1)
        # Reversing each partition restores the order within both pieces.
        reverse(0, k - 1)
        # The first k reversed elements are exactly the former suffix.
        reverse(k, len(nums) - 1)
        # The method mutates nums and intentionally returns None.


if __name__ == "__main__":
    solution = Solution()
    values = [1, 2, 3, 4, 5, 6, 7]
    assert solution.rotate(values, 3) is None
    assert values == [5, 6, 7, 1, 2, 3, 4]
    values = [-1, -100, 3, 99]
    solution.rotate(values, 2)
    assert values == [3, 99, -1, -100]
    values = [1, 2]
    solution.rotate(values, 4)
    assert values == [1, 2]
    print("All tests passed")
