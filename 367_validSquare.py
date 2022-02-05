class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num== 1:
            return True
        
        n = 2
        while (n-1)**2 +2*n-1 <num:
            n+=1
        if (n-1)**2 +2*n-1 == num:
            return True
        else: return False
