class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        if n==0:
            return tri[0]
        elif n==1:
            return tri[1]
        elif n==2:
            return tri[2]
        else:
            for i in range(3, n+1):
                tri.append(tri[i-1]+tri[i-2]+tri[i-3])
            return tri[n]
