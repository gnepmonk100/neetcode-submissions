class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        ways_to_climb = [0]*(n+1)

        ways_to_climb[0] = 1
        ways_to_climb[1] = 1

        for idx in range(2,n+1):
            ways_to_climb[idx] = ways_to_climb[idx-1] + ways_to_climb[idx-2]

        return ways_to_climb[n]




