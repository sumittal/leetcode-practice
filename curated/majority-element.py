from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # candidate represents the unmatched value in the current prefix.
        # balance is the candidate's excess over canceled alternatives.
        candidate = None
        balance = 0
        for value in nums:
            # A zero balance starts a new cancellation block at this value.
            if balance == 0:
                candidate = value
            # Matching values reinforce the candidate; others cancel one vote.
            balance += 1 if value == candidate else -1
            # A candidate change always occurs only after the balance reaches zero.
        # More than half the input belongs to the guaranteed majority.
        # Therefore cancellation cannot leave a different final candidate.
        # This vote pass does not require a frequency table.
        return candidate


if __name__ == "__main__":
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([7]) == 7
    print("All tests passed")
