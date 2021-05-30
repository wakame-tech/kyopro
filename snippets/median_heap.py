import heapq
import bisect


class MedianHeap:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def remove(self, num: int):
        """ O(N) """
        i = bisect.bisect_left(self.max_heap, num)
        if i < len(self.max_heap):
            self.max_heap[i] = self.max_heap[-1]
            self.max_heap.pop()
            heapq.heapify(self.max_heap)

        i = bisect.bisect_left(self.min_heap, num)
        if i < len(self.min_heap):
            self.min_heap[i] = self.min_heap[-1]
            self.min_heap.pop()
            heapq.heapify(self.min_heap)

    def add(self, num: int):
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        if not self.max_heap:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            return
        if len(self.max_heap) == len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

    def median(self) -> float:
        # rtype: float
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]


def test_median_heap():
    mh = MedianHeap()
    mh.add(1)
    mh.add(2)
    mh.add(3)
    assert mh.median() == 2
    mh.add(4)
    mh.add(5)
    assert mh.median() == 3
    mh.remove(4)
    mh.remove(5)
    assert mh.median() == 2

test_median_heap()