class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengths = []

        for start_idx in range(len(s)):
            seen = []
            longest = 0

            for idx in range(start_idx, len(s)):
                if s[idx] not in seen:
                    seen.append(s[idx])
                    longest += 1
                else:
                    break
            lengths.append(longest)
        return max(lengths)
