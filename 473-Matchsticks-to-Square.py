class Solution(object):
    def makesquare(self, matchsticks):
        \\\
        :type matchsticks: List[int]
        :rtype: bool
        \\\
        target = sum(matchsticks) 
        if target % 4 != 0:
            return False 
        target = target // 4 
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        def backtracking(i):
            if i == len(matchsticks):
                return True 
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i] 
                    if backtracking(i+1):
                        return True
                    sides[j] -= matchsticks[i] 
                    if sides[j] == 0:
                        break
            return False 
        return backtracking(0)