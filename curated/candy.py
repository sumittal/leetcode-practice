from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        # One candy is the lower bound for every child.
        candies = [1] * len(ratings)
        # A rising left-to-right slope constrains each child against the left.
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1
            # Equal and falling edges need no extra candy in this pass.
        # The reverse pass enforces descending slopes against the right neighbor.
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                # Keep whichever directional constraint requires more candies.
                candies[index] = max(candies[index], candies[index + 1] + 1)
            # Taking max preserves any increasing-slope requirement already met.
        # Both neighbor directions are now satisfied for every adjacent pair.
        # Summing gives the minimum because each pass adds only necessary candies.
        return sum(candies)


if __name__ == "__main__":
    solution = Solution()
    assert solution.candy([1, 0, 2]) == 5
    assert solution.candy([1, 2, 2]) == 4
    assert solution.candy([1, 3, 4, 5, 2]) == 11
    assert solution.candy([5]) == 1
    print("All tests passed")
