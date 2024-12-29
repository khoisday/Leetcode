class Solution(object):
    def generate(self, numRows):
        \\\
        :type numRows: int
        :rtype: List[List[int]]
        \\\
        memo = {}

        def F(i,j):
            if (i,j) in memo:
                return memo[i,j]

            if j == 0 or j == i:
                return 1

            returnedValue = F(i - 1, j - 1) + F(i - 1, j)
            memo[i,j] = returnedValue
            return returnedValue

        ans = [[-1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                ans[i][j] = F(i, j)
        
        return ans
