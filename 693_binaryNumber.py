class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = format(n,"b")
        k=0
        for i in range(len(n)-1):
            if n[i+1]==n[i]:
                return False
                break
            k+=1
        if k == len(n) -1:
            return True
