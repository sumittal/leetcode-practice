"""
LeetCode 3822: Design Order Management System
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+3822+Design+Order+Management+System+neetcode
Complexity:
    - Time: add/modify/cancel O(1) expected, query O(k)
    - Space: O(n)
"""

from collections import defaultdict
from typing import DefaultDict, Dict, List, Optional, Set, Tuple


class OrderManagementSystem:
    def __init__(self):
        # ID lookup supports updates; the reverse set supports exact-price queries.
        self.orders: Dict[int, Tuple[str, int]] = {}
        self.buckets: DefaultDict[Tuple[str, int], Set[int]] = defaultdict(set)

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        # Direct ID replacement keeps the primary and reverse indexes in sync.
        self.orders[orderId] = (orderType, price)
        self.buckets[(orderType, price)].add(orderId)
        # Set membership prevents duplicate IDs in a bucket.

    def _remove_from_bucket(self, order_id: int) -> None:
        order_type, price = self.orders[order_id]
        key = (order_type, price)
        # Use the stored order type and price rather than caller-supplied values.
        self.buckets[key].remove(order_id)
        # Empty reverse buckets have no future query value.
        if not self.buckets[key]:
            del self.buckets[key]

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        order_type, _ = self.orders[orderId]
        self._remove_from_bucket(orderId)
        self.orders[orderId] = (order_type, newPrice)
        self.buckets[(order_type, newPrice)].add(orderId)
        # Repricing is a move between reverse-index buckets.

    def cancelOrder(self, orderId: int) -> None:
        # Remove the reverse entry before deleting the canonical order record.
        self._remove_from_bucket(orderId)
        del self.orders[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        # The problem permits any output order; the replay sorts for stable checks.
        # Exact bucket lookup avoids scanning all live orders.
        return list(self.buckets.get((orderType, price), set()))


def replay(
    ops: List[str], args: List[List[object]]
) -> List[Optional[List[int]]]:
    outputs: List[Optional[List[int]]] = []
    manager = None
    for operation, values in zip(ops, args):
        if operation == "OrderManagementSystem":
            manager = OrderManagementSystem()
            outputs.append(None)
        else:
            result = getattr(manager, operation)(*values)
            outputs.append(sorted(result) if operation == "getOrdersAtPrice"
                           else None)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["OrderManagementSystem", "addOrder", "addOrder", "getOrdersAtPrice",
         "modifyOrder", "getOrdersAtPrice", "cancelOrder", "getOrdersAtPrice"],
        [[], [4, "buy", 10], [5, "buy", 10], ["buy", 10], [4, 11],
         ["buy", 10], [5], ["buy", 10]],
    ) == [None, None, None, [4, 5], None, [5], None, []]
    assert replay(
        ["OrderManagementSystem", "addOrder", "addOrder", "cancelOrder",
         "getOrdersAtPrice"],
        [[], [1, "sell", 20], [2, "buy", 20], [1], ["sell", 20]],
    ) == [None, None, None, None, []]
    print("All tests passed")
