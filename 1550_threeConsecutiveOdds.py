class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        k = 0
        for i in range(len(arr)):
            if k==3:
                return True
            if arr[i]%2!=0:
                k+=1
            else:
                k=0
        if k==3:
            return True
        return False
