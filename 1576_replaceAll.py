class Solution:
    def modifyString(self, s: str) -> str:
        s = [" "]+ list(s) + [" "]
        for i in range(1,len(s)):
            if s[i] == "?":
                for j in ["a","b","c"]:
                    if j!=s[i-1] and j!=s[i+1]:
                        s[i]=j
                        break
        return "".join(s[1:len(s)-1])
