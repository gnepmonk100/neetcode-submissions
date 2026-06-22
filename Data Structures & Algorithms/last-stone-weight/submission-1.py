import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heavy1 = -heapq.heappop(max_heap)
            heavy2 = -heapq.heappop(max_heap)

            if heavy1 != heavy2:
                heapq.heappush(max_heap, -(heavy1-heavy2))
            
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]

        