class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for idx in range(len(nums)):
            if nums[idx] not in seen:
                seen.add(nums[idx])
            else:
                return nums[idx]
        


        