class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) ==2:
            return True
        for i in range(len(arr)):
            if arr[i] ==0:
                continue
            elif arr[i]/2 in arr or arr[i]*2 in arr:
                return True
        return False
