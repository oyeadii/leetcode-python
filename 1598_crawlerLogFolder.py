class Solution:
    def minOperations(self, logs: List[str]) -> int:
        k = 0
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if k!=0:
                    k-=1
            else:
                k+=1
        return k
