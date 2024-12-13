class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:  
            result += n & 1  
            n >>= 1 
        return result