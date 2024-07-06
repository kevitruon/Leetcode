class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices),1):
                diff = prices[j]-prices[i]
                largest = max(largest,diff)
        return largest