class Solution:
    def reverse(self, x: int) -> int:
        k=0
        if x < 0:
            x = abs(x)
            k+=1
        x  = list(map(int, str(x)))
        y = 0
        for i in range(len(x)):
            y+=x[i]*(10**i)
        if y not in range((-2**31), (2**31 -1)):
            return 0
        else:
            if k==0:
                return y
            else:
                return -y
