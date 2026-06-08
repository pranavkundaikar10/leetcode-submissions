class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0
        while r < len(prices):
            print(l, r, prices[l], prices[r])
            if prices[r] < prices[l]:
                print("lesser price")
                l = r
                continue
            max_profit = max(max_profit, prices[r]-prices[l])
            print('profit', max_profit)
            r += 1
        return max_profit
        
        