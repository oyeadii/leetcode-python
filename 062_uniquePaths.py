class Solution:
    def uniquePaths(self, m: int, n: int, arr={}) -> int:
        key = str(m) +','+str(n)
        key1 = str(n)+','+str(m)
        if key in arr:
            return arr[key]
        if key1 in arr:
            return arr[key1]
        if m==0 or n==0:
            return 0
        if m==1 and n==1:
            return 1
        arr[key] = self.uniquePaths(m-1,n, arr) + self.uniquePaths(m, n-1, arr)
        return arr[key]
