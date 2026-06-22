class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string: keep only letters/numbers and lowercase them
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Your exact same two-pointer logic
        left = 0
        right = len(cleaned_str) - 1

        while left <= right:
            if cleaned_str[left] == cleaned_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
       
        