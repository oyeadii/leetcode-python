class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst = set()
        for num in nums:
            if num not in lst:
                lst.add(num)
            else:
                return True
        return False
