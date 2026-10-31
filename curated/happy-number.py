class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # Repeating a value proves the deterministic sequence has entered a cycle.
        # Every digit-square transform eventually reaches a small finite value range.
        while n != 1 and n not in seen:
            seen.add(n)
            # Replace n by the sum of squares of its decimal digits.
            next_value = 0
            while n:
                digit = n % 10
                next_value += digit * digit
                n //= 10
                # Zero digits add nothing but are consumed by the same division step.
            # The next iteration checks the new value before expanding it again.
            n = next_value
        # Reaching one is success; any other repeated state is an unhappy cycle.
        # The repeated value need not be the first member of the cycle.
        # Storing visited states bounds work by the number of distinct sequence values.
        return n == 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.isHappy(19) is True
    assert solution.isHappy(2) is False
    assert solution.isHappy(1) is True
    assert solution.isHappy(7) is True
    print("All tests passed")
