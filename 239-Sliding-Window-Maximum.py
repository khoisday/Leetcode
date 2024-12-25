from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \\\
        res = []
        queue = deque()
        for i, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()

            queue.append(num)

            if i >=k and nums[i - k] == queue[0]:
                queue.popleft()

            if i >= k - 1:
                res.append(queue[0])

        return res