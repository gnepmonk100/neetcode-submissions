class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 1
        possible_starts = []
        if len(nums) == 0:
            return 0
        for num in nums:
            if num-1 in nums:
                continue
            else:
                possible_starts.append(num)

        for start in possible_starts:
            start_len = 1
            next_num = start + 1
            while next_num in nums:
                next_num +=1
                start_len +=1
            if start_len > longest_len:
                longest_len = start_len
        return longest_len
        