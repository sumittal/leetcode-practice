from typing import List, Optional


class BrowserHistory:
    # A list plus cursor models the currently reachable path through history.
    def __init__(self, homepage: str):
        # The homepage is always the first reachable history entry.
        self.history: List[str] = [homepage]
        # The cursor is an index so back and forward are constant-time moves.
        self.current = 0

    def visit(self, url: str) -> None:
        # A visit creates a new branch and removes every page ahead of the cursor.
        self.history = self.history[: self.current + 1]
        self.history.append(url)
        self.current += 1
        # Forward pages are no longer reachable after the new branch is added.

    def back(self, steps: int) -> str:
        # Clamp movement to the earliest page retained in the history list.
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Clamp movement to the last page previously visited.
        self.current = min(len(self.history) - 1, self.current + steps)
        # A page index never moves outside the retained list.
        return self.history[self.current]


def replay(
    ops: List[str], args: List[List[object]]
) -> List[Optional[str]]:
    outputs: List[Optional[str]] = []
    browser = None
    for operation, values in zip(ops, args):
        if operation == "BrowserHistory":
            browser = BrowserHistory(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(browser, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["BrowserHistory", "visit", "visit", "visit", "back", "back",
         "forward", "visit", "forward", "back", "back"],
        [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"],
         [1], [1], [1], ["linkedin.com"], [2], [2], [7]],
    ) == [
        None, None, None, None, "facebook.com", "google.com",
        "facebook.com", None, "linkedin.com", "google.com", "leetcode.com",
    ]
    assert replay(
        ["BrowserHistory", "back", "forward", "visit", "forward"],
        [["home"], [10], [10], ["new"], [1]],
    ) == [None, "home", "home", None, "new"]
    print("All tests passed")
