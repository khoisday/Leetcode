class Solution(object):
    def combinationSum(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        candidates.sort()  # Sort array first
        res = []
        
        def backtrack(remain, comb, start):  # Added start parameter
            if remain == 0:
                res.append(comb[:])  # Make a copy of combination
                return
            
            for i in range(start, len(candidates)): 
                if candidates[i] > remain:
                    break
                
                backtrack(remain - candidates[i], comb + [candidates[i]], i)
                
        backtrack(target, [], 0)
        return res