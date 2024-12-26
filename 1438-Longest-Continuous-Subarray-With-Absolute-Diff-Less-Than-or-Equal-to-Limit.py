class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        increase, decrease = deque(), deque()
        l = 0
        max_len = 0

        for r in range (n):
            while decrease and decrease[-1] < nums[r]:
                decrease.pop()
            decrease.append(nums[r])

            while increase and increase[-1] > nums[r]:
                increase.pop()
            increase.append(nums[r])

            while abs(increase[0] - decrease[0]) > limit:
                if nums[l] == increase[0]:
                    increase.popleft()
                elif nums[l] == decrease[0]:
                    decrease.popleft()
                
                l += 1

            max_len = max(max_len, r - l + 1)
            
        return max_len
