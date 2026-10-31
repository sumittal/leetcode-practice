from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search the shorter input to minimize partition adjustments.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        first_length = len(nums1)
        second_length = len(nums2)
        left = 0
        right = first_length
        half = (first_length + second_length + 1) // 2
        # The partition puts half the combined elements on its left side.
        # The extra one for odd totals keeps the median among the left-side values.
        while left <= right:
            first_cut = (left + right) // 2
            second_cut = half - first_cut
            # Boundary sentinels let empty partitions use the same comparisons.
            first_left = nums1[first_cut - 1] if first_cut else float("-inf")
            first_right = (
                nums1[first_cut] if first_cut < first_length else float("inf")
            )
            second_left = nums2[second_cut - 1] if second_cut else float("-inf")
            second_right = (
                nums2[second_cut]
                if second_cut < second_length
                else float("inf")
            )
            if first_left <= second_right and second_left <= first_right:
                # Both cross-boundaries are ordered, so this is the valid split.
                # Internal order is already guaranteed by each input being sorted.
                left_middle = max(first_left, second_left)
                if (first_length + second_length) % 2:
                    # An odd total has one central value on the left partition.
                    return float(left_middle)
                right_middle = min(first_right, second_right)
                # Even totals average the largest left and smallest right values.
                return (left_middle + right_middle) / 2.0
            if first_left > second_right:
                # Too many small-array elements are on the left; move its cut left.
                right = first_cut - 1
            else:
                # The small-array cut is too far left to order both partitions.
                left = first_cut + 1
            # Moving one cut determines the other, preserving the total left partition size.
        # Inputs are sorted and at least one is nonempty, so a partition must exist.
        return 0.0


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert solution.findMedianSortedArrays([], [1]) == 1.0
    assert solution.findMedianSortedArrays([2], []) == 2.0
    print("All tests passed")
