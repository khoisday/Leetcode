class Solution(object):
    def nextGreaterElements(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[int]
        \\\
        n = len(nums)
        stack = []
        result = [-1] * n
        
        
        for i in range(2*n-1, -1, -1):
            curr_num = nums[i % n]
            
            while stack and stack[-1] <= curr_num:
                stack.pop()
            
            if stack:
                result[i % n] = stack[-1]
                
            stack.append(curr_num)
            
        return result