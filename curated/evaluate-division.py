from collections import defaultdict, deque
from typing import Dict, List, Tuple


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        # Equation orientation determines the multiplier along each graph edge.
        # Each edge stores the multiplier needed when traversing its equation.
        graph: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1.0 / value))
            # Reciprocal edges allow queries in either direction.
            # The original ratio is retained on its forward edge.
        answers = []
        for start, target in queries:
            if start not in graph or target not in graph:
                answers.append(-1.0)
                continue
            # BFS carries the product from the query numerator to each node.
            queue = deque([(start, 1.0)])
            visited = {start}
            answer = -1.0
            while queue:
                variable, product = queue.popleft()
                if variable == target:
                    answer = product
                    break
                for neighbor, ratio in graph[variable]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * ratio))
                # Each variable is explored once for this query.
                # Consistent equations give the same product along every valid path.
            answers.append(answer)
        # A known variable reaches itself with the initial product of one.
        return answers


if __name__ == "__main__":
    solution = Solution()
    answers = solution.calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    assert all(abs(left - right) < 1e-9 for left, right in zip(answers, expected))
    answers = solution.calcEquation(
        [["a", "b"], ["c", "d"]],
        [1.0, 1.0],
        [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
    )
    expected = [-1.0, -1.0, 1.0, 1.0]
    assert all(abs(left - right) < 1e-9 for left, right in zip(answers, expected))
    assert solution.calcEquation([], [], [["x", "x"]]) == [-1.0]
    print("All tests passed")
