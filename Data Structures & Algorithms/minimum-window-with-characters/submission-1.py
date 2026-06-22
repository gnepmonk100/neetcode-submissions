from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
            
        # Dictionary to keep a count of all the unique characters in t.
        t_count = Counter(t)
        
        # Dictionary to keep track of characters in the current sliding window.
        window_count = {}
        
        # 'required' is the number of unique characters in t that must be present in our window.
        # 'formed' tracks how many unique characters currently meet their target frequency.
        required = len(t_count)
        formed = 0
        
        # Tuple to store the look of our window: (window length, left index, right index)
        # Initialized with float("inf") so any real window will be smaller.
        ans = (float("inf"), None, None)
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the current character's frequency matches its required frequency in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
                
            # Try and contract the window from the left until it is no longer valid.
            while left <= right and formed == required:
                char_left = s[left]
                
                # Update our smallest window found so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # The character at the 'left' pointer is about to be discarded
                window_count[char_left] -= 1
                if char_left in t_count and window_count[char_left] < t_count[char_left]:
                    formed -= 1
                    
                # Move the left pointer forward to look for a smaller window
                left += 1
                
        # If ans[0] was never updated, it means no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]