class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                k+=1

        return k
