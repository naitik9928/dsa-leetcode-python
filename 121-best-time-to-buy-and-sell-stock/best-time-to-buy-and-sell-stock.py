class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_go=prices[0]
        for i in prices:
            if i <min_go:
                min_go=i
            if max_profit<i-min_go:
                max_profit=i-min_go
        return max_profit