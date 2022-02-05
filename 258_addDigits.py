class Solution:
    def addDigits(self, num: int) -> int:
        lst =[]
        while len(lst) !=1:
            add=0
            lst = list(map(int,str(num)))
            for i in range(len(lst)):
                add += lst[i]
            num = add
        return add
