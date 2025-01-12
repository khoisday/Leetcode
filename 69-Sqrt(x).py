class Solution(object):
    def mySqrt(self, x):
        \\\
        :type x: int
        :rtype: int
        \\\
        left, right = 0, x
        res = -1

        while left <= right:
            mid = (left + right)  // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
                res = mid
            else:
                res = mid
                return res

        return res