from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = [False, False, False]
        # These flags only move from false to true as usable candidates are scanned.
        # Any coordinate overshooting the target disqualifies the whole triplet.
        for triplet in triplets:
            if any(value > goal for value, goal in zip(triplet, target)):
                continue
            # A usable triplet may contribute any subset of its exact target coordinates.
            for index in range(3):
                if triplet[index] == target[index]:
                    matched[index] = True
            # A candidate never lowers coordinates already supplied by earlier triplets.
            # Taking coordinate-wise maxima allows different candidates to supply each value.
            # Coordinate maxima may come from different usable triplets.
            if all(matched):
                return True
        # All three target coordinates must have been supplied by some allowed triplet.
        # No combination can repair a coordinate that no usable triplet matches.
        # Keeping only flags is sufficient because the target itself is the upper bound.
        return all(matched)


if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeTriplets(
        [[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]
    ) is True
    assert solution.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) is False
    assert solution.mergeTriplets(
        [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]
    ) is True
    assert solution.mergeTriplets([[1, 1, 1]], [1, 1, 1]) is True
    print("All tests passed")
