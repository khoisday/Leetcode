class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,0
        shortest_size = float("inf")
        curr_sum = 0
        for r in range (len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                shortest_size = min(shortest_size, r-l +1)
                curr_sum -= nums[l]
                l += 1            
        
        if shortest_size == float("inf"):
            return 0
        else:
            return shortest_size
            


        