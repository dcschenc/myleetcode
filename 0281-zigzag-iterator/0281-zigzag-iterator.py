from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()
        for idx, v in enumerate(self.vectors):        
            if len(v) > 0:
                self.queue.append((idx, 0))

    def next(self) -> int:
        idx, cur = self.queue.popleft()
        data = self.vectors[idx][cur]
        if cur + 1 < len(self.vectors[idx]):
            self.queue.append((idx, cur + 1))
        return data

    def hasNext(self) -> bool:
        return self.queue

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())