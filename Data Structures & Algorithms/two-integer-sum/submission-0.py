class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for index in range(0, len(nums)-1):
            other_num = target - nums[index]
            if other_num in nums:
                indices.append(index)
                indices.append(nums.index(other_num))
                return indices


        