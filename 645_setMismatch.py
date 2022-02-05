class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum1 = sum(nums)
        nums = set(nums)
        sum2 = sum(nums)
        sum3 = (n*(n+1))//2
        return [sum1-sum2, sum3-sum2]
                
        
