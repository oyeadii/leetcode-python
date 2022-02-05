class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=0
        k=0
        lst=[]
        while j!=len(numbers)-k-1:
            if numbers[j] + numbers[len(numbers)-k-1] >target:
                k+=1
            elif numbers[j] + numbers[len(numbers)-k-1] <target:
                j+=1
            else:
                lst.append(j+1)
                lst.append(len(numbers)-k)
                return lst
                break
