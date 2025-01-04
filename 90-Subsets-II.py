class Solution(object):
    def subsetsWithDup(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        res = []
        comb = []
        nums.sort()

        def dfs(comb, start):
            res.append(comb[:])

            for i in range (start, len(nums)):
                if i> start and nums[i] == nums[i-1] :
                    continue

                comb.append(nums[i])
                dfs(comb, i+1)
                comb.pop()

        dfs([], 0)
        return res