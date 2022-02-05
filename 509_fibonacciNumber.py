class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        if n==0:
            return arr[0]
        elif n==1:
            return arr[1]
        else:
            for i in range(2,n+1):
                arr.append(arr[i-1]+arr[i-2])
            return arr[n]
