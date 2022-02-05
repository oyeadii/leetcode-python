class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []
        if nums.count(target) ==0:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    lst.append(i)
                    break
            lst.append(i+nums.count(target)-1)
            return lst
