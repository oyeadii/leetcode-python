class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: 
            return 1.0000
        elif x ==0:
            return 0
        else:
            val = self.myPow(x,abs(n)//2)
            if n%2==1:
                val1 = val*val*x
            else:
                val1 = val*val
            if n>0:
                return val1
            else:
                return 1/val1
