class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[-1]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range (2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]

