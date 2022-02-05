class Solution:
    def findComplement(self, num: int) -> int:
        dict={"0":"1","1":"0"}
        b = ''.join(dict[x] for x in format(num,"b"))
        b = list(b)
        c = 0
        for i in range(len(b)):
            c +=int(b[len(b)-i-1])*(2**i)
        return c
