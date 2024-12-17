# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        newHead = None
        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next

        return newHead

    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
            
        # Find middle
        mid = self.findMid(head)
        
        # Reverse second half
        second_half = self.reverse(mid)
        
        # Compare first half with reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True
        