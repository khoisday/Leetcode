class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if (arr[m] > arr[m + 1]):
                r = m
            else:
                l = m + 1

        return l
        