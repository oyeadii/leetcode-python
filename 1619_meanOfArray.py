class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(0.05*len(arr))
        sum1 = (sum(arr[n:len(arr)-n]))/len(arr[n:len(arr)-n])
        
        return sum1
