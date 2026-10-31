from typing import Dict, List, Optional


class FreqStack:
    # Frequency groups preserve recency among values tied at that frequency.
    # The maximum frequency determines which group supplies the next pop.
    def __init__(self):
        # Frequencies track current multiplicity after each pop.
        self.frequency: Dict[int, int] = {}
        # Each group stores push recency for one exact frequency.
        self.groups: Dict[int, List[int]] = {}
        self.maximum = 0

    def push(self, val: int) -> None:
        frequency = self.frequency.get(val, 0) + 1
        self.frequency[val] = frequency
        # The frequency stack records recency among values reaching this count.
        self.groups.setdefault(frequency, []).append(val)
        # A new maximum frequency is reached only by incrementing one value.
        self.maximum = max(self.maximum, frequency)

    def pop(self) -> int:
        value = self.groups[self.maximum].pop()
        self.frequency[value] -= 1
        # The removed value no longer belongs to its former frequency group.
        # Emptying the top group exposes the next lower active frequency.
        if not self.groups[self.maximum]:
            self.maximum -= 1
        return value


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    stack = None
    for operation, values in zip(ops, args):
        if operation == "FreqStack":
            stack = FreqStack()
            outputs.append(None)
        else:
            outputs.append(getattr(stack, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FreqStack", "push", "push", "push", "push", "push", "push",
         "pop", "pop", "pop", "pop"],
        [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
    ) == [None, None, None, None, None, None, None, 5, 7, 5, 4]
    assert replay(
        ["FreqStack", "push", "push", "pop", "pop"],
        [[], [9], [9], [], []],
    ) == [None, None, None, 9, 9]
    print("All tests passed")
