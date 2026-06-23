class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')' : '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map and stack:
                top_element = stack.pop()
                if top_element == bracket_map[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        return True
        


        

        