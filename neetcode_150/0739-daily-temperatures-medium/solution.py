"""
LeetCode 739: Daily Temperatures
Difficulty: Medium
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=cTBiBSnjO3c
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Unresolved indices stay on a stack in decreasing temperature order.
        answer = [0] * len(temperatures)
        waiting = []
        # Each index is pushed once and stays pending until resolved or the end.
        # Zero is the correct default for a day with no warmer future temperature.
        for day, temperature in enumerate(temperatures):
            # This warmer day resolves every earlier cooler day at the stack top.
            while waiting and temperatures[waiting[-1]] < temperature:
                previous_day = waiting.pop()
                answer[previous_day] = day - previous_day
                # This is the first warmer day because intervening days were processed.
            # Equal temperatures remain unresolved because they are not warmer.
            waiting.append(day)
        # Entries never resolved by a warmer day correctly retain zero.
        # Each index is pushed and popped once, so all stack operations amortize to O(n).
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert solution.dailyTemperatures([30, 30]) == [0, 0]
    assert solution.dailyTemperatures([]) == []
    print("All tests passed")
