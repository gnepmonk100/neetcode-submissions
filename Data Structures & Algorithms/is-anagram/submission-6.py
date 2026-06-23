class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for char_s in s:
            if char_s in dict_s:
                dict_s[char_s] += 1
            else:
                dict_s[char_s] = 1
        for char_t in t:
            if t in dict_t:
                dict_s[char_t] += 1
            else:
                dict_t[char_t] = 1

        for char in dict_s.keys():
            if char in dict_t.keys():
                if dict_t[char] == dict_t[char]:
                    continue
            else:
                return False
        return True

        