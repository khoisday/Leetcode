# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        \\\
        :type head: ListNode
        :rtype: ListNode
        \\\
        oneJump = twoJump = head
        while twoJump and twoJump.next:
            oneJump = oneJump.next
            twoJump = twoJump.next.next
            if oneJump == twoJump:
                break
        else: return None
        twoJump = head
        while twoJump != oneJump:
            twoJump, oneJump = twoJump.next, oneJump.next

        return twoJump
