from bisect import bisect_left, bisect_right, insort
from collections import defaultdict
from typing import Dict, List


class TweetCounts:
    # Bucket endpoints are inclusive and frequency widths are fixed in seconds.
    # Timestamp arrays remain independent for each tweet name.
    def __init__(self):
        # Sorted times allow bucket counts through binary-search boundaries.
        # Each tweet name has an independent time series.
        self.times: Dict[str, List[int]] = defaultdict(list)
        self.width = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        # Insertion keeps times ordered even when timestamps arrive out of order.
        insort(self.times[tweetName], time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        width = self.width[freq]
        times = self.times[tweetName]
        result: List[int] = []
        # The final bucket is clipped to the inclusive requested endpoint.
        bucket_start = startTime
        # Advancing by a fixed width creates every bucket including empty ones.
        while bucket_start <= endTime:
            bucket_end = min(endTime, bucket_start + width - 1)
            left = bisect_left(times, bucket_start)
            right = bisect_right(times, bucket_end)
            result.append(right - left)
            # The next bucket begins immediately after this inclusive endpoint.
            bucket_start += width
        return result


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    counts = None
    for op, values in zip(ops, args):
        if op == "TweetCounts":
            counts = TweetCounts()
            outputs.append(None)
        else:
            result = getattr(counts, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TweetCounts", "recordTweet", "recordTweet", "recordTweet",
         "getTweetCountsPerFrequency", "getTweetCountsPerFrequency",
         "recordTweet", "getTweetCountsPerFrequency"],
        [[], ["tweet3", 0], ["tweet3", 60], ["tweet3", 10],
         ["minute", "tweet3", 0, 59], ["minute", "tweet3", 0, 60],
         ["tweet3", 120], ["hour", "tweet3", 0, 210]],
    ) == [None, None, None, None, [2], [2, 1], None, [4]]
    print("All tests passed")
