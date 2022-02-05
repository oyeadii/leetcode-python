class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        k=0
        j=0
        for i in range(len(nums)):
            if i%2==0:
                arr.append(nums[k])
                k+=1
            else:
                arr.append(nums[j+n])
                j+=1
        return arr
