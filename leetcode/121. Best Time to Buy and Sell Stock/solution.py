class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_day = 0
        sell_day = 0

        while sell_day < len(prices):
            buy_price = prices[buy_day]
            sell_price = prices[sell_day]

            if buy_price > sell_price:
                buy_day = sell_day
            else:
                local_profit = sell_price - buy_price
                profit = local_profit if local_profit > profit else profit

            sell_day += 1

        return profit
 
