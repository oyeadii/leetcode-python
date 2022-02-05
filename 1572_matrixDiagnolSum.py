class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        n = len(mat)
        for i in range(n):
            sum1+= mat[i][i] + mat[i][n-i-1]
        if len(mat)%2!=0:
            sum1-= mat[n//2][n//2]
        return sum1
