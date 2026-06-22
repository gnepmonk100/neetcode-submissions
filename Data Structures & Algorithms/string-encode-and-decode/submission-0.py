class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: <length>#<string>
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # Find the delimiter starting from current index i
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length and convert to integer
            length = int(s[i:j])
            
            # Move i to the start of the actual string content
            i = j + 1
            
            # Slice the string based on the parsed length
            res.append(s[i : i + length])
            
            # Move i to the start of the next encoded block
            i += length
            
        return res