class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = set(range(1, len(nums)+1))
        nums = set(nums)
        return list(arr-nums)
        
