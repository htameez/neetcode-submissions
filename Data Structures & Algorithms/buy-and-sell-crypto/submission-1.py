class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        # set aside profit array with max profit you can make at each index
        # access previous profits from the array; profit = sell - buy (minimum value to left of i)

        if len(prices) == 1:
            return 0

        maxProfits = [0] * len(prices)

        for i in range(1, len(prices)):
            maxProfits[i] = prices[i] - min(prices[0:i])
        
        return max(maxProfits)
