from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Edges point from a prerequisite to the course it unlocks.
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, before in prerequisites:
            # Each listed prerequisite contributes one incoming edge to its course.
            graph[before].append(course)
            indegree[course] += 1
        # Zero-indegree courses have no unfinished requirements and may be taken now.
        queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
        # completed counts the acyclic prefix removed from the dependency graph.
        completed = 0
        while queue:
            course = queue.popleft()
            # Each dequeued course is now safely removed from the remaining graph.
            completed += 1
            # Completing a course removes one incoming dependency from each successor.
            for following in graph[course]:
                indegree[following] -= 1  # Remove this satisfied prerequisite edge.
                if indegree[following] == 0:
                    queue.append(following)
        # A cycle leaves at least one course with a prerequisite still outstanding.
        return completed == numCourses


if __name__ == "__main__":
    solution = Solution()
    assert solution.canFinish(2, [[1, 0]]) is True
    assert solution.canFinish(2, [[1, 0], [0, 1]]) is False
    assert solution.canFinish(1, []) is True
    assert solution.canFinish(3, [[0, 0]]) is False
    print("All tests passed")
