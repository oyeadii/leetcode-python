class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in accounts:
            sum1 = sum(i)
            if sum1 > maximum:
                maximum= sum1
        return maximum
