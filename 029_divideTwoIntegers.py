class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend<0) != (divisor<0)
        dividend = abs(dividend)
        divisor =  abs(divisor)

        temp=divisor
        temp1 = dividend
        n=1
        ans=0
        while temp1>=temp:
            temp1-=temp
            ans+=n
            n+=n
            temp+=temp
            if temp1<temp:
                n=1
                temp = divisor
            

        if neg:
            return max(-ans,-2147483648)
        else:
            return min(ans,2147483647)
