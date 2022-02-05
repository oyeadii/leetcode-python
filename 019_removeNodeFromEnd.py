class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        if temp is None:
            return
        i=0
        j=1
        while temp:
            i+=1
            temp =temp.next
        temp = head

        i = i-n+1
        if i ==1:
            head = temp.next
            return head
        else:
            prev = temp
            while j!=i:
                prev = temp
                temp = temp.next
                j+=1
            prev.next = temp.next
            return head 
            
