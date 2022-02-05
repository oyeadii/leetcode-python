class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            print("")
        current = strs[0]
        print(current)
        for i in range(1,len(strs)):
            temp=""
            if len(current)==0:
                break
            for j in range(len(strs[i])):
                if j<len(current) and current[j]== strs[i][j]:
                    temp+=current[j]
                else:
                    break
            current=temp
        return current
