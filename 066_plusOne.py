class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num = num + digits[i]*(10**(len(digits)-1-i))
        num +=1
        b = list(map(int,str(num)))
        return b  
