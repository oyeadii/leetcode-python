class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            k=0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    k+=1
            lst.append(k)

        return lst
