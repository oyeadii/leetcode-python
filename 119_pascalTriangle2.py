class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from math import factorial
        for i in range(rowIndex+1):
            a = []
            for j in range(i+1):
                a.append(factorial(i)//(factorial(j)*factorial(i-j)))
        return a
                
