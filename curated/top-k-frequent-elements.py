from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        # A value can occur at most len(nums) times, bounding valid bucket indices.
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, frequency in frequencies.items():
            buckets[frequency].append(value)

        result = []
        # Frequency zero is empty; scan nonempty buckets from most to least frequent.
        for frequency in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[frequency])
            # Once k values are collected, all remaining buckets are lower frequency.
            if len(result) >= k:
                return result[:k]
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]
    assert sorted(solution.topKFrequent([4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(solution.topKFrequent([1, 2, 2, 3, 3], 3)) == [1, 2, 3]
    print("All tests passed")
