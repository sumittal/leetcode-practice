class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first = len(a) - 1
        # Both operands are read-only; only their cursors move.
        second = len(b) - 1
        carry = 0
        # Output digits are collected backward to avoid front insertion.
        reversed_bits = []
        # Indices move from least-significant bits toward the leading bits.
        while first >= 0 or second >= 0 or carry:
            total = carry
            # Missing digits contribute zero after either string is exhausted.
            if first >= 0:
                total += int(a[first])
                first -= 1
            if second >= 0:
                total += int(b[second])
                second -= 1
            # Division by two gives the next carry and current output bit.
            reversed_bits.append(str(total % 2))
            # A total of three emits one and carries one into the next column.
            carry = total // 2
            # Keep the carry in the loop condition for a possible extra bit.
        # Reverse once after collecting digits in arithmetic order.
        return "".join(reversed(reversed_bits))


if __name__ == "__main__":
    solution = Solution()
    assert solution.addBinary("11", "1") == "100"
    assert solution.addBinary("1010", "1011") == "10101"
    assert solution.addBinary("0", "0") == "0"
    assert solution.addBinary("1", "0") == "1"
    print("All tests passed")
