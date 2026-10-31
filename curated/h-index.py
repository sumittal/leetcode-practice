from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Descending order makes index i the number i + 1 of leading papers.
        # Sorting a copy avoids mutating the citations passed by the caller.
        ordered = sorted(citations, reverse=True)
        h = 0
        for rank, count in enumerate(ordered, start=1):
            # A rank qualifies when that many papers each meet its citation bar.
            if count < rank:
                break
            # Every earlier rank qualified because the counts are descending.
            h = rank
            # Larger ranks cannot qualify after the first failed threshold.
        # Sorting a copy preserves the caller's citation order.
        # The largest qualifying rank is the h-index definition.
        # A zero result covers empty citations and papers with no citations.
        return h


if __name__ == "__main__":
    solution = Solution()
    assert solution.hIndex([3, 0, 6, 1, 5]) == 3
    assert solution.hIndex([1, 3, 1]) == 1
    assert solution.hIndex([0, 0]) == 0
    print("All tests passed")
