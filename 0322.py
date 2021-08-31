class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        depth = 1
        values = set(coins)
        seen = set()
        
        while min(values) <= amount:
            new = set()
            for value in values:
                if value == amount:
                    return depth
                
                if value not in seen:
                    possibilities = [value + coin for coin in coins]
                    seen.add(value)
                    new.update(possibilities)

            values = new  
            depth += 1
        
        return -1