class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=0
        length = len(s)
        num1=0
        num2=0
        for i in range(length-1,0,-1):
            if s[i] == ' ':
                while s[len(s)-1-j] ==  ' ':
                    num1 = length-1-j
                    j+=1
                while s[length-1-j] !=  ' ':
                    num2 = len(s)-1-j
                    j+=1
                break
            if s[length-1] != ' ':
                num1= length-1
                while s[len(s)-1-j] !=  ' ' and length-1-j>=0:
                    j+=1
                num2= len(s)-1-j
                break
        if len(s)==1 and s[0]==' ':
            return 0
        elif len(s)==1 and s[0]!=' ':
            return 1
        else:
            return num1-num2
