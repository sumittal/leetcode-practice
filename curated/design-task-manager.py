import heapq
from typing import Dict, List, Optional, Tuple


class TaskManager:
    # Current task records live in a map, while the heap may contain stale versions.
    # Priority and task-ID negation implement the platform's descending order.
    def __init__(self, tasks: List[List[int]]):
        # Task IDs are unique, so one current record per task is sufficient.
        self.tasks: Dict[int, Tuple[int, int]] = {}
        self.heap: List[Tuple[int, int, int]] = []
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def _push(self, user_id: int, task_id: int, priority: int) -> None:
        self.tasks[task_id] = (user_id, priority)
        # Negated priority and ID implement the required descending tie order.
        heapq.heappush(self.heap, (-priority, -task_id, user_id))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self._push(userId, taskId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id, _ = self.tasks[taskId]
        # A new heap record supersedes the older record without linear removal.
        self._push(user_id, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # Lazy invalidation avoids searching the heap for this task.
        self.tasks.pop(taskId, None)

    def execTop(self) -> int:
        # Discard stale records until the heap's highest live task is found.
        while self.heap:
            negative_priority, negative_task_id, user_id = heapq.heappop(self.heap)
            task_id = -negative_task_id
            priority = -negative_priority
            # Stale records fail this comparison after edit or removal.
            if self.tasks.get(task_id) == (user_id, priority):
                del self.tasks[task_id]
                return user_id
        return -1


def replay(ops: List[str], args: List[list]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    manager = None
    for operation, values in zip(ops, args):
        if operation == "TaskManager":
            manager = TaskManager(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(manager, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"],
        [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5],
         [102, 8], [], [101], [5, 105, 15], []],
    ) == [None, None, None, 3, None, None, 5]
    assert replay(
        ["TaskManager", "add", "add", "execTop", "execTop"],
        [[[]], [1, 10, 7], [2, 11, 7], [], []],
    ) == [None, None, None, 2, 1]
    print("All tests passed")
