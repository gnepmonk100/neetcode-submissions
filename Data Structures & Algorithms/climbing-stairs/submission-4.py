class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1

        for idx in range(2, n+1):
            temp = cur
            cur = prev + cur
            prev = temp
        return cur

       