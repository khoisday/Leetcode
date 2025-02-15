# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        \\\
        :type n: int
        :rtype: int
        \\\
        if n == 1:
            return 1
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1                    

            else:
                l = mid + 1
                
            