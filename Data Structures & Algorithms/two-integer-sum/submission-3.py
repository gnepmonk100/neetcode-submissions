class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map stores: { value: index }
        prev_map = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                # We found the pair!
                return [prev_map[diff], i]
            
            # Store the current number and its index
            prev_map[n] = i
        