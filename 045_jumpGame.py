class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        jumps=0
        maximum = 0
        current=0
        for i in range(len(nums)-1):
            if i+nums[i] >maximum:
                maximum=i+nums[i]
            if current == i:
                jumps+=1
                current = maximum
        return jumps
