class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
        k=0
        for i in range(len(n)-1,-1,-1):
            if k==3:
                n.insert(i+1,".")
                k=1
            else:
                k+=1
        return "".join(n)
