class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [(amount+1)] * (amount + 1)
        minCoins[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    minCoins[i] = min(minCoins[i], minCoins[i - c] + 1)
        if minCoins[amount] != (amount+1):
            return minCoins[amount]
        else:
            return -1
        
            
