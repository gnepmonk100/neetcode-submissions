class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        
        for idx in range(2*n):
            if idx < n:
                ans[idx] = nums[idx]
            else:
                ans[idx] = nums[idx-n]
        return ans