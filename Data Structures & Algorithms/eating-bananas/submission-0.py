class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        min_speed = upper_bound

        Left = 1
        Right = upper_bound
        M = (Left + Right) // 2

        while Left <= Right:
            total_time = 0

            M = (Left + Right) // 2

            for pile in piles:
                total_time +=  math.ceil(float(pile)/M)
            
            if total_time <= h:
                min_speed = M
                Right = M - 1
            elif total_time > h:
                Left = M + 1
        return min_speed






   


        
