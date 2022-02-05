class Solution:
    def convertToBase7(self, num: int) -> str:
        a =[]
        if num>0:
            while num!=0:
                a.append(str(num%7))
                num = num//7
            a.reverse()
            return ''.join(a)
        elif num==0:
            return '0'
        else:
            num = abs(num)
            while num!=0:
                a.append(str(num%7))
                num = num//7
            a.reverse()
            a.insert(0,'-')
            return ''.join(a)
