class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 
        profit = 0
        while l < len(prices)-1:
            if prices[l] < prices[r]:
                profit = profit + (prices[r] - prices[l])


            l += 1
            r += 1
                        
        return profit
    


s = Solution()
print(s.maxProfit(prices = [7,6,4,3,1]))    