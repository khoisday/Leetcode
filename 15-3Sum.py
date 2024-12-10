class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n -2:
            target = 0 - nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (nums[j] == nums[j - 1] and j < n - 1):
                        j += 1
                    while (nums[k] == nums[k + 1] and k > j):
                        k -= 1
                    continue
                if nums[j] + nums[k] < target:
                    j += 1
                    continue
                else:
                    k -=1

            i += 1
            while nums[i] == nums[i - 1] and i < n -2:
                i += 1


        return result