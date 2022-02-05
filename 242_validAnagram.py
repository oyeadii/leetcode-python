class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s =  list(s)
            t = list(t)
            s.sort()
            t.sort()
            for i in range(len(t)):
                if t[i] == s[i]:
                    continue
                else:
                    return False
            return True
