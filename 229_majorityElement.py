class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n =len(nums)
        c1 = 0 
        c2 = 0
        num1 = -1
        num2 = -1
        for i in nums:
            if i == num1:
                c1+=1
            elif i == num2:
                c2+=1
            elif c1 ==0:
                num1 = i
                c1 =1
            elif c2 ==0:
                num2 = i
                c2 =1
            else:
                c1-=1
                c2-=1
        count1 =0
        count2 =0
        for i in nums:
            if i == num1:
                count1+=1
            elif i == num2:
                count2+=1
        res = []
        if count1 > n//3:
            res.append(num1)
        if count2 > n//3:
            res.append(num2)
        return res
            
