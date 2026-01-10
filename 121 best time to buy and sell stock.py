"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
#solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        if len(prices)<2:
            return 0
        Min = prices[-2]
        Max = prices[-1]
        prof = Max-Min
        for i in range(len(prices)-1, -1, -1):
            if Max<prices[i]:
                for j in range(i, -1, -1):
                    if prices[i]-prices[j]>prof:
                        prof = prices[i] - prices[j]
                Max = prices[i]
            else:
                if Min>prices[i]:
                    if prof<Max-prices[i]:
                        prof = Max - prices[i]
                    Min = prices[i]
        if prof<0:
            return 0     
        return prof