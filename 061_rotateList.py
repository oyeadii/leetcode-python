# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp1 = head
        n=0
        while temp1:
            n+=1
            temp1 =temp1.next
        k = k%n
        for i in range(k):
            temp = head
            while temp.next != None:
                prev = temp
                temp = temp.next
            temp.next = head
            prev.next = None
            head = temp
        
        return head
