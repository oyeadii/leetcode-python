class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        from math import factorial
        arr = []
        for i in range(numRows):
            a=[]
            for j in range(i+1):
                a.append(factorial(i)//(factorial(j)*factorial(i-j)))
            arr.append(a)
        return arr
