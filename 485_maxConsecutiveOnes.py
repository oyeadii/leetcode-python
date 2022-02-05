class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        maximum = 0
        for i in nums:
            if i==1:
                k+=1
            else:
                if k >maximum:
                    maximum = k
                k=0
        if k>maximum:
            maximum=k
        return maximum
