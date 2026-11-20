class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max= 0
        for i in range(len(prices)):

            l, r = prices[i], prices[len(prices)-1]
            profit= l - r

            if profit < 0:
                l += 1
                r -= 1

            elif profit >= 0:
                if profit > max:
                    max = profit
        return max