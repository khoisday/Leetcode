class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        l = 0
        max_length = 0
        
        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                max_length = max(max_length, r - l + 1)
            
            seen[char] = r
            
        return max_length