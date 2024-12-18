\\\
Idea: Reverse the 2nd half of the linked list and compare it with the first half.

Time complexity: O(n)

Space Complexity: O(n)
\\\

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, curr):
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
    
    def findMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        mid = self.findMid(head)
        secondHalf = self.reverse(mid)
        
        while secondHalf:
            if head.val != secondHalf.val:
                return False
            head = head.next
            secondHalf = secondHalf.next

        return True