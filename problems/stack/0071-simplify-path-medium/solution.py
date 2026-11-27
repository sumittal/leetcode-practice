"""
LeetCode 71: Simplify Path
Difficulty: Medium
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=qYlHrAKJfyA
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Empty components and current-directory markers do not change location.
        # Splitting turns slash-delimited path syntax into independent tokens.
        directories = []
        for component in path.split("/"):
            if component in ("", "."):
                continue
            # Parent traversal removes one directory but never leaves root.
            if component == "..":
                if directories:
                    directories.pop()
            else:
                # Ordinary names are preserved as literal directory components.
                directories.append(component)
            # Stack order matches the final path from root outward.
            # A normal directory name is never interpreted as a path operator.
        # One leading slash makes the result absolute and canonical.
        # Joining once avoids repeated string rewriting as components are processed.
        return "/" + "/".join(directories)


if __name__ == "__main__":
    solution = Solution()
    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/home//foo/") == "/home/foo"
    assert solution.simplifyPath("/a/./b/../../c/") == "/c"
    print("All tests passed")
