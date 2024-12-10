class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i, num in enumerate(nums):
            find_num = target - num
            
            if find_num in seen:
                return [i, seen[find_num]]
                
            seen[num] = i
            
        return []