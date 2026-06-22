class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # We look for the 'complement' (the number needed to reach target)
            complement = target - nums[i]
            
            # We only look at numbers AFTER the current index 'i'
            # to avoid using the same element twice.
            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    return [i, j]
       
        