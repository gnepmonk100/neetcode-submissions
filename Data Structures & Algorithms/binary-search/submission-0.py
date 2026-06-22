class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0 
        R = N-1
        M = (L+R)//2
        idx = -1

        while L<=R:
            M = (L+R)//2

            if nums[M] == target:
                idx = M
                return idx
            elif target < nums[M]:
                R = M-1
            else:
                L = M+1
        return idx
        