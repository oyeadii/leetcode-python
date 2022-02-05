class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k =0
        while k<len(arr):
            if arr[k]==0:
                arr.insert(k,0)
                arr.pop(len(arr)-1)
                k+=2
            else:
                k+=1
