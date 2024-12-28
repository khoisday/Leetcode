class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        prev = 0
        ans = 0

        for i in range (len(values)):
            ans = max(ans, prev + values[i] - i)
            prev = max(prev, values[i] + i)

        return ans