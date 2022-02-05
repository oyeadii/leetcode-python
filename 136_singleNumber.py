class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = nums.count(nums[i])
            if a ==1:
                break
        return nums[i]
