class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Fix 1: Initialize the list with 0s matching the input size
        days = [0] * len(temperatures)

        for idx1 in range(len(temperatures)):
            for idx2 in range(idx1 + 1, len(temperatures)):
                if temperatures[idx2] > temperatures[idx1]:
                    # Fix 2: Directly calculate the distance using the indices
                    days[idx1] = idx2 - idx1
                    break # Stop looking forward for idx1 once found
                    
        return days