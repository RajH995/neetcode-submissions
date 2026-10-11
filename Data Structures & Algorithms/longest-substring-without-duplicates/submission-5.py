class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        longest = 0
        # Use a dictionary to store the last seen index of each character
        char_map = {}
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            char_map[s[right]] = right
            current_len = right - left + 1
            if current_len > longest:
                longest = current_len
                
        return longest