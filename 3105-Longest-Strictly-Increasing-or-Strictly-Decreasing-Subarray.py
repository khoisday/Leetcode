class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_len = 1
        decrease_len = 1
        increase_max = 1
        decrease_max = 1
        
        for i in range (1, len(nums)):
            if nums[i] > nums[i-1]:
                increase_len += 1
                increase_max = max(increase_len, increase_max)
                decrease_len = 1
            elif nums[i] < nums[i - 1]:
                decrease_len += 1
                decrease_max = max(decrease_len, decrease_max)
                increase_len = 1
            else:
                increase_len, decrease_len = 1, 1

        return increase_max if increase_max > decrease_max else decrease_max
