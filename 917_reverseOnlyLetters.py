class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        lo = 0
        hi = len(s)-1
        while lo <hi:
            if ord(s[lo].lower()) not in range(97,123):
                lo+=1
            if ord(s[hi].lower()) not in range(97,123):
                hi-=1
            if (ord(s[lo].lower()) in range(97,123)) and (ord(s[hi].lower()) in range(97,123)):
                temp = s[lo]
                s[lo] = s[hi]
                s[hi] =temp
                lo+=1
                hi-=1
        return "".join(s)
