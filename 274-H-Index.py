class Solution(object):
    def hIndex(self, citations):
        \\\
        :type citations: List[int]
        :rtype: int
        \\\
        n = len(citations)
        citations.sort()

        for index, cite in enumerate(citations):
            if cite >= n - index:
                return n - index
        
        return 0
