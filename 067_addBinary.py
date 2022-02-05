class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        inta=0
        intb=0
        for item in a:
            inta += int(item)*(2**i)
            i-=1
        for item in b:
            intb += int(item)*(2**j)
            j-=1
        return format(inta+intb,"b")
