# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        temp = None
        while slow:
            next = slow.next
            slow.next = temp
            temp = slow
            slow = next
        while temp:
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next
            
        return True
