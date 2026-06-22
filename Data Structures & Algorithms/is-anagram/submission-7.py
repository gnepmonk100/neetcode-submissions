class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick exit: if lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        # Correctly counting characters for s
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
            
        # Correctly counting characters for t
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Simply compare the two dictionaries
        return dict_s == dict_t