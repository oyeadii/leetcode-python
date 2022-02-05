class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        num1 = 0
        num2=0
        for i in range(len(s)):
            num2 += ord(s[i])
        for i in range(len(t)):
            num1 += ord(t[i])
        return chr(num1-num2)
