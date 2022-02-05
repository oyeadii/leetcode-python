class Solution:
    def maximum69Number (self, num: int) -> int:
        maxNum = 9999
        lst = list(map(str,str(num)))
        if num == maxNum:
            return num
        else:
            for i in range(len(lst)):
                if lst[i] == '6':
                    lst.remove(lst[i])
                    lst.insert(i,'9')
                    break
            return int(''.join(lst))
