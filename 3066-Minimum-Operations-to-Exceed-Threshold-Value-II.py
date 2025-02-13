import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        heapq.heapify(nums)
        count = 0
        
        while len(nums) >= 2 and nums[0] < k:
            count += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            newNum = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, newNum)
        
        if nums[0] < k:
            return -1
            
        return count