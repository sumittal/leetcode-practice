from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # The last m positions of nums1 are spare capacity, not input values.
        left = m - 1
        right = n - 1
        write = m + n - 1
        # The largest unmerged value always belongs in the current write slot.
        # Filling from the end preserves every unconsumed value in nums1.
        while right >= 0:
            # When nums1 is exhausted, nums2 supplies the next largest value.
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[write] = nums1[left]
                left -= 1
            else:
                # Equal values are safe to take from nums2 first.
                nums1[write] = nums2[right]
                right -= 1
            # Each assignment closes exactly one slot at the right boundary.
            write -= 1
            # The unprocessed prefixes remain sorted after each comparison.
        # Any remaining nums1 prefix is already in its final position.
        # Exhausting nums2 is sufficient because nums1 begins sorted.


if __name__ == "__main__":
    solution = Solution()
    first = [1, 2, 3, 0, 0, 0]
    solution.merge(first, 3, [2, 5, 6], 3)
    assert first == [1, 2, 2, 3, 5, 6]
    second = [1]
    solution.merge(second, 1, [], 0)
    assert second == [1]
    third = [0]
    solution.merge(third, 0, [1], 1)
    assert third == [1]
    print("All tests passed")
