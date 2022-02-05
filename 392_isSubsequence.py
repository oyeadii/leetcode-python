class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)> len(t):
            return False
        elif len(s) == len(t):
            if s==t:
                return True
            else:
                return False
        else:
            i = 0
            j= 0
            while i< len(s):
                if j > len(t)-1:
                    return False
                if s[i] == t[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            return True
