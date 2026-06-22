class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        # 2. Use a Min-Heap to keep track of the top k elements
        # We store (freq, num) so the heap sorts by frequency
        min_heap = []
        
        for num, count in frequency.items():
            heapq.heappush(min_heap, (count, num))
            # If the heap size exceeds k, pop the element with the smallest frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # 3. Extract the numbers from the heap
        return [item[1] for item in min_heap]

        