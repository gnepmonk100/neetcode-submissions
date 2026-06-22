class Solution:
    def climbStairs(self, n: int) -> int:
        
        ways_to_climb = {0:1, 1:1}

        def climb(x):
            if x in ways_to_climb:
                return ways_to_climb[x]
            else:
                ways_to_climb[x] = climb(x-1) + climb(x-2)
                return ways_to_climb[x]
        
        num_ways = climb(n)
        return num_ways
        