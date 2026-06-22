class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            heavy1 = stones[-1]
            heavy2 = stones[-2]

            if heavy1 == heavy2:
                stones.pop()
                stones.pop()
            elif heavy2 < heavy1:
                stones.pop()
                stones.pop()
                stones.append(heavy1-heavy2)
            stones.sort()
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
        