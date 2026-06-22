import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        k_points = []

        for point in points:
            x_coord = point[0]
            y_coord = point[1]

            distance = ((x_coord**2 + y_coord**2)**0.5)
            
            heapq.heappush(max_heap, (-distance, point ))
        
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for entry in max_heap:
            k_points.append(entry[1])
        
        return k_points
        





        

