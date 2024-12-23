class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        \\\
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        \\\
        hashMap = {}
        result = []
        stack = []
        for i in reversed(nums2):
            while stack:
                if stack[-1] > i:
                    hashMap[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop()

            if not stack:
                hashMap[i] = -1
                stack.append(i)

        for i in nums1:
            result.append(hashMap[i])

        return result
