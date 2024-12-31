class Solution(object):
    def combinationSum2(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        candidates.sort()
        res = []

        def backtrack(sum, start, comb):
            if sum < 0:
                return

            if sum == 0:
                res.append(comb)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                if candidates[i] > sum:
                    break
                
                backtrack(sum - candidates[i], i + 1, comb + [candidates[i]])

        backtrack(target, 0, [])
        return res