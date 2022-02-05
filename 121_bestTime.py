class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minprice = 100001
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            elif (prices[i]-minprice)> maximum:
                maximum = prices[i]-minprice
        
        return maximum
