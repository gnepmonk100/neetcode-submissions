class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        bracket_map = {")": "(", "}": "{", "]": "["}

        for idx in range(int(n//2)):
            if s[idx] == bracket_map[s[n-1-idx]]:
                continue
            else:
                return False
        return True


        