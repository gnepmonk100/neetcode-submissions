class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_length = len(nums)
        max_numbers = []
        for idx in range(0, nums_length - k + 1):
            numbers_in_window = []
            for num in nums[idx: idx+k]:
                numbers_in_window.append(num)
            
            max_numbers.append(max(numbers_in_window))
        return max_numbers

        