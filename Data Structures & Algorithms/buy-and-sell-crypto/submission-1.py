class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        maxprofit=0
    
        while j <len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxprofit = max (maxprofit,profit)

            else:
                i=j
            j+=1
        return maxprofit


        