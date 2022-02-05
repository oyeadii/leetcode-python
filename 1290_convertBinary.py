# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        i=0
        dec = 0
        if temp is None:
            return 
        while temp != None:
            i+=1
            temp = temp.next
        temp =head
        while temp != None:
            dec += (temp.val)*(2**(i-1))
            temp = temp.next
            i-=1
        return dec
        
