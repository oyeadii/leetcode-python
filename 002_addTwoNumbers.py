class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listToInt(ln):
            result = 0
            digit = 1
            while ln:
                result += digit*ln.val
                ln = ln.next
                digit *= 10
            return result
        sum1 = str(listToInt(l1) + listToInt(l2))
        node = None
        for s in sum1:
            node = ListNode(int(s),node)
        return node
