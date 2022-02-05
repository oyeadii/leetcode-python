class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>0.9 and n!=1:
            n=n/4

        if int(n) ==1:
            return True
        else:
            return False
