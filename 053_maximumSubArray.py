class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        maximum = arr[0]
        for i in range(1,len(nums)):
            arr.append(max(arr[i-1]+nums[i], nums[i]))
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum
