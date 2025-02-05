class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        diff_index = []
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                diff_index.append(i)
                if diff > 2:
                    return False
        
        if diff == 1:
            return False
        if diff == 0:
            return True
            
        # Check if swapping would make strings equal
        return s1[diff_index[0]] == s2[diff_index[1]] and s1[diff_index[1]] == s2[diff_index[0]]

        
