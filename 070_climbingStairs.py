class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        n1 = 1
        n2 = 2

        while count < n-1:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return n1
