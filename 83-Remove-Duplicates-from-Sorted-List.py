# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        temp = head
        while (head and head.next):
            if head.next.val == head.val:
                head.next = head.next.next
                continue

            head = head.next

        return temp
            

