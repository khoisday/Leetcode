class Solution(object):
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        
        # If target is not reachable or the transformation is invalid
        if (target + total_sum) % 2 != 0 or target > total_sum or target < -total_sum:
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # Initialize DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0: use no numbers
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]