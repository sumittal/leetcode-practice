import heapq
from typing import Dict, List, Optional, Union


class VideoSharingPlatform:
    def __init__(self):
        # Only active IDs live in these dictionaries.
        self.videos: Dict[int, str] = {}
        self.views: Dict[int, int] = {}
        self.likes: Dict[int, int] = {}
        self.dislikes: Dict[int, int] = {}
        self.reusable: List[int] = []
        self.next_id = 0

    def upload(self, video: str) -> int:
        # Freed IDs are reused in ascending order before allocating new ones.
        if self.reusable:
            video_id = heapq.heappop(self.reusable)
        else:
            video_id = self.next_id
            self.next_id += 1
        self.videos[video_id] = video
        # New uploads always start with fresh engagement counters.
        self.views[video_id] = 0
        self.likes[video_id] = 0
        self.dislikes[video_id] = 0
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId not in self.videos:
            return
        del self.videos[videoId]
        del self.views[videoId]
        del self.likes[videoId]
        del self.dislikes[videoId]
        # The min-heap makes the smallest removed ID available next.
        heapq.heappush(self.reusable, videoId)
        # Removing an absent ID does not create a duplicate reusable entry.

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        video = self.videos.get(videoId)
        if video is None:
            return "-1"
        # Views count successful watches, even when the requested range is short.
        self.views[videoId] += 1
        # The end point is inclusive, so slice one position beyond it.
        return video[startMinute : min(endMinute + 1, len(video))]

    def like(self, videoId: int) -> None:
        # Engagement is ignored for IDs that are not currently active.
        if videoId in self.videos:
            self.likes[videoId] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.dislikes[videoId] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        # The two counters are kept separately to match the API result.
        if videoId not in self.videos:
            return [-1]
        return [self.likes[videoId], self.dislikes[videoId]]

    def getViews(self, videoId: int) -> int:
        return self.views.get(videoId, -1)


def replay(
    ops: List[str], args: List[List[object]]
) -> List[Optional[Union[int, str, List[int]]]]:
    outputs: List[Optional[Union[int, str, List[int]]]] = []
    platform = None
    for operation, values in zip(ops, args):
        if operation == "VideoSharingPlatform":
            platform = VideoSharingPlatform()
            outputs.append(None)
        else:
            outputs.append(getattr(platform, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["VideoSharingPlatform", "upload", "watch", "watch", "like",
         "dislike", "getLikesAndDislikes", "getViews", "remove", "getViews",
         "upload"],
        [[], ["123"], [0, 0, 5], [0, 2, 5], [0], [0], [0], [0], [0], [0],
         ["456"]],
    ) == [None, 0, "123", "3", None, None, [1, 1], 2, None, -1, 0]
    assert replay(
        ["VideoSharingPlatform", "watch", "like", "getLikesAndDislikes",
         "upload", "remove", "remove", "upload"],
        [[], [8, 0, 1], [8], [8], ["7"], [0], [0], ["9"]],
    ) == [None, "-1", None, [-1], 0, None, None, 0]
    print("All tests passed")
