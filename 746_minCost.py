class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i1=0
        i2=0
        for i in range(2,len(cost)+1):
            i2, i1 = i1, min(i1+ cost[i-1], i2 + cost[i-2])
        return i1 
