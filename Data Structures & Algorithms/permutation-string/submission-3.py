class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        s1_dict = {}

        for char in s1:
            if s1 in s1_dict:
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1


        for idx in range(n-m+1):
            substring_dict = {}
            for char in s2[idx: idx+m]:
                
                if char in substring_dict:
                    substring_dict[char] += 1
                else:
                    substring_dict[char] = 1
            if substring_dict == s1_dict:
                return True
        return False

        