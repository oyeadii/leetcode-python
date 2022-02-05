class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n+1):
            a.append((format(i,"b")).count('1'))

        return a
