class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        numRows = len(mat)
        numCols = len(mat[0])
        rows = [0] * numRows
        cols = [0] * numCols

        map = {}
        for i in range (numRows):
            for j in range (numCols):
                map[mat[i][j]] = [i , j]

        for index, num in enumerate(arr):
            r, c = map[num][0],  map[num][1]

            rows[r] += 1
            cols[c] += 1

            if rows[r] == numCols or cols[c] == numRows:
                return index
