class Solution(object):
    def subsets(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        subset = []
        result = []
        self.generateSubset(0, subset, nums, result)
        return result
        
    def generateSubset(self, index, subset, nums, result):
        if index == len(nums):
            result.append(subset[:]) 
            return
        
        # Include nums[index]
        subset.append(nums[index])
        self.generateSubset(index + 1, subset, nums, result)
        subset.pop()
        
        # Exclude nums[index]
        self.generateSubset(index + 1, subset, nums, result)