class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        square = 0
        for j in range(10):
            lst = list(map(int,str(temp)))
            for i in range(len(lst)):
                square += (lst[i])**2
            temp=square
            square=0
            if temp==1:
                return True
                break
        if temp!=1:
            return False
