class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        i = j = k
        min_val = nums[k]
        max_score = min_val

        while i > 0 or j < n - 1:
            left_val = nums[i-1] if i > 0 else 0
            right_val = nums[j+1] if j < n - 1 else 0

            if left_val < right_val and j < n - 1:
                j+=1
                min_val = min(min_val, nums[j])

            elif left_val >= right_val and i > 0:
                i-=1
                min_val = min(min_val, nums[i])

            else:
                break

            max_score = max(max_score, (j-i+1) * min_val)

        return max_score