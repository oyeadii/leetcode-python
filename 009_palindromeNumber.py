class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(map(str,str(x)))
        num = len(a)
        final =0
        if a[0] == '-':
            return False

        else:
            for i in range(num):
                final = int(a[num-i-1])*(10**(num-i-1)) + final
           
            if x ==final:
                return True
            else: 
                return False
