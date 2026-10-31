from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: convert least-significant-first values to a linked list.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: read list digits in their stored least-significant-first order.
def list_values(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # A dummy head keeps appending result digits uniform, including the first.
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            # Missing digits contribute zero while the longer operand continues.
            first_digit = l1.val if l1 is not None else 0
            second_digit = l2.val if l2 is not None else 0
            total = first_digit + second_digit + carry
            carry, digit = divmod(total, 10)
            # Store only this column's digit; divmod carries the tens to the next.
            tail.next = ListNode(digit)
            # Extend the result tail once for each input digit column processed.
            tail = tail.next
            # Advance only lists that still have a digit in this column.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        # The loop condition emits a final node whenever addition leaves a carry.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.addTwoNumbers(build_list([2, 4, 3]), build_list([5, 6, 4]))
    ) == [7, 0, 8]
    assert list_values(
        solution.addTwoNumbers(build_list([0]), build_list([0]))
    ) == [0]
    assert list_values(
        solution.addTwoNumbers(
            build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9])
        )
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert list_values(solution.addTwoNumbers(build_list([1]), build_list([9, 9]))) == [
        0,
        0,
        1,
    ]
    print("All tests passed")
