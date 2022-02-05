class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums)
        a=0
        b = nums.count(nums[0])
        if b==len(nums):
            return max(nums)
        elif len(nums)>2:
            for i in range(3):
                a = nums.count(nums[k-i-1])
                for j in range(a-1):
                    k-=1
            return nums[k-i-1]
        else:
            return max(nums)
