class Solution:
    def findMin(self, nums: List[int]) -> int:
        Left = 0
        Right = len(nums) - 1

        while Left < Right:
            M = (Left + Right-1) // 2

            if nums[M] < nums[Right]:
                Right = M
            else:
                Left = M + 1
        return nums[Left]
        