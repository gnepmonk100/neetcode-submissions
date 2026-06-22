class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Create an empty array
        cleaned_array = []
        
        # 2. Loop through and append valid characters
        for char in s:
            if char.isalnum():
                cleaned_array.append(char.lower())
        
        # 3. Your two-pointer logic works exactly the same on an array!
        left = 0
        right = len(cleaned_array) - 1

        while left <= right:
            if cleaned_array[left] == cleaned_array[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
       
        