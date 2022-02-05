class Solution:
    def reverseBits(self, n: int) -> int:
        n = list("{:032b}".format(n))
        n.reverse()
        n = ''.join(n)
        num =0
        for i in range(len(n)):
            num+= int((n[len(n)-i-1]))*(2**i)
        return num
