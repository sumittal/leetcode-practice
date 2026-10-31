from typing import Dict, List, Optional


class TodoList:
    def __init__(self):
        # IDs are global and never reused, even after a task is completed.
        self.tasks: Dict[int, Dict[int, dict]] = {}
        self.next_task_id = 1

    def addTask(
        self, userId: int, taskDescription: str, dueDate: int, tags: List[str]
    ) -> int:
        task_id = self.next_task_id
        # Monotonic allocation prevents a completed task ID from being reused.
        self.next_task_id += 1
        task = {
            "description": taskDescription,
            "due": dueDate,
            "tags": set(tags),
        }
        # Per-user storage makes ownership checks direct and local.
        self.tasks.setdefault(userId, {})[task_id] = task
        return task_id

    def _pending(self, userId: int) -> List[dict]:
        user_tasks = self.tasks.get(userId, {})
        # Unique due dates define a total order without a secondary tie rule.
        # Sorting once lets both list methods share the same order guarantee.
        return sorted(user_tasks.values(), key=lambda task: task["due"])

    def getAllTasks(self, userId: int) -> List[str]:
        return [task["description"] for task in self._pending(userId)]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        # Filtering after due-date ordering preserves the required result order.
        return [
            task["description"]
            for task in self._pending(userId)
            if tag in task["tags"]
        ]

    def completeTask(self, userId: int, taskId: int) -> None:
        # A user's dictionary also enforces ownership of each task ID.
        self.tasks.get(userId, {}).pop(taskId, None)
        # A missing ID or a task owned by another user is a no-op.


def replay(ops: List[str], args: List[List[object]]) -> List[Optional[object]]:
    outputs: List[Optional[object]] = []
    todo = None
    for operation, values in zip(ops, args):
        if operation == "TodoList":
            todo = TodoList()
            outputs.append(None)
        else:
            outputs.append(getattr(todo, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TodoList", "addTask", "addTask", "getAllTasks", "getTasksForTag",
         "completeTask", "getAllTasks"],
        [[], [1, "later", 4, ["work"]], [1, "soon", 2, ["work", "urgent"]],
         [1], [1, "urgent"], [1, 2], [1]],
    ) == [None, 1, 2, ["soon", "later"], ["soon"], None, ["later"]]
    assert replay(
        ["TodoList", "addTask", "addTask", "completeTask", "getAllTasks"],
        [[], [1, "mine", 1, []], [2, "other", 2, []], [1, 2], [2]],
    ) == [None, 1, 2, None, ["other"]]
    print("All tests passed")
