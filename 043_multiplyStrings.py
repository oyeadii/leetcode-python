class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        for i in range(len(num1)):
            a+=(ord(num1[i])-48)*(10**(len(num1)-1-i))
        for i in range(len(num2)):
            b+=(ord(num2[i])-48)*(10**(len(num2)-1-i))
        return str(a*b)
