from collections import deque
from typing import List


def is_valid_order(
    num_courses: int, prerequisites: List[List[int]], order: List[int]
) -> bool:
    # A topological order must include every course exactly once.
    if len(order) != num_courses or set(order) != set(range(num_courses)):
        return False
    positions = {course: index for index, course in enumerate(order)}
    # Every prerequisite must appear earlier than the course that depends on it.
    return all(
        positions[prerequisite] < positions[course]
        for course, prerequisite in prerequisites
    )


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edges run from each prerequisite toward the course it unlocks.
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        # Incoming-edge counts track prerequisites that remain unfinished.
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        # Only courses with no remaining prerequisites may start the order.
        ready = deque(course for course, degree in enumerate(indegree) if degree == 0)
        order = []
        while ready:
            course = ready.popleft()
            # Each course is appended once when its final prerequisite is removed.
            order.append(course)
            # Completing a course satisfies one incoming dependency for each successor.
            for following in graph[course]:
                indegree[following] -= 1
                if indegree[following] == 0:
                    ready.append(following)
        # A cycle leaves some courses unscheduled, so no full ordering exists.
        # Returning any complete Kahn order is valid; its exact tie order is arbitrary.
        return order if len(order) == numCourses else []


if __name__ == "__main__":
    solution = Solution()
    prerequisites = [[1, 0]]
    order = solution.findOrder(2, prerequisites)
    assert is_valid_order(2, prerequisites, order)
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(4, prerequisites, order)
    assert solution.findOrder(2, [[1, 0], [0, 1]]) == []
    assert is_valid_order(3, [], solution.findOrder(3, []))
    print("All tests passed")
