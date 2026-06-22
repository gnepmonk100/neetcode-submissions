import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Transform the input list into a valid Min-Heap in-place
        heapq.heapify(self.heap)
        
        # 2. Chop down the heap until it only holds the 'k' largest elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap) # Removes the smallest element from the top

    def add(self, val: int) -> int:
        # 1. Push the new value onto our heap
        heapq.heappush(self.heap, val)
        
        # 2. If pushing it made the heap exceed size k, pop the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. The top of the min-heap (index 0) is guaranteed to be the k-th largest
        return self.heap[0]