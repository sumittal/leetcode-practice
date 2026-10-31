class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # A one-row path never changes direction or row grouping.
        if numRows == 1 or numRows >= len(s):
            return s
        # Each bucket stores characters in the order they visit one row.
        rows = [""] * numRows
        current_row = 0
        direction = 1
        # Direction is a signed step that keeps the current row in bounds.
        for character in s:
            rows[current_row] += character
            # Boundary rows reverse travel so the next character follows the zigzag.
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
            # Every input character is appended exactly once.
            # The repeated down/up traversal defines the full zigzag cycle.
        # Reading buckets top-to-bottom is the required row-wise output.
        # Direct row buckets avoid allocating unused grid cells.
        return "".join(rows)


if __name__ == "__main__":
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
    assert solution.convert("AB", 3) == "AB"
    print("All tests passed")
