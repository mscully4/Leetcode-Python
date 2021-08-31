class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        
        def traverse(stair):
            if n - stair == 1:
                return 1
            elif n - stair == 2:
                return 2
            else:
                if stair not in mem:
                    result = traverse(stair + 1) + traverse(stair + 2)
                    mem[stair] = result
                    return result
                else:
                    return mem[stair]
            
        return traverse(0)
        