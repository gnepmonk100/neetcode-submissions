class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is longer than s, it's impossible to find a valid window
        if len(s) < len(t):
            return ""

        substr_length = {}

        # Loop through every possible starting position in string s
        for start_idx in range(len(s)):
            # Create a fresh copy of the characters we need to find
            letters = list(t)
            
            # Use a second pointer to explore forward from our start position
            curr_idx = start_idx
            
            # Keep moving forward as long as we haven't found all letters 
            # AND we haven't run off the edge of string s
            while len(letters) > 0 and curr_idx < len(s):
                char = s[curr_idx]
                if char in letters:
                    letters.remove(char)
                curr_idx += 1  # Safely move to the next character

            # If letters is empty, it means we successfully found a valid window!
            if len(letters) == 0:
                # The valid substring stretches from start_idx up to curr_idx
                valid_substring = s[start_idx:curr_idx]
                
                # Store the substring using its length as the key
                # Note: If two substrings have the same length, this overwrites it,
                # which is fine since we only need *any* minimum window.
                substr_length[len(valid_substring)] = valid_substring
        
        # If our dictionary is completely empty, no valid window was ever found
        if not substr_length:
            return ""
            
        # Find the smallest key (length) and return its corresponding substring
        min_length = min(substr_length.keys())
        return substr_length[min_length]