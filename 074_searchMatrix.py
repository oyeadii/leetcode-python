class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        k = -1
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                k = i
        if k == -1:
            return False
        for i in range(n):
            if matrix[k][i] == target:
                return True
        return False
