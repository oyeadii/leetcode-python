class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            j = s.count(s[i])
            if j==1:
                return i
                break
        return -1
