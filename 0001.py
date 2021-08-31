class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        
        for i in range(len(nums)):
            r = mem.get(nums[i], [])
            r.append(i)
            mem[nums[i]] = r
            
        for x in range(len(nums)):
            comp = target - nums[x]
            r = mem.get(comp, None)
            
            if r and len(r) == 1 and r[0] != x:
                return [x, r[0]]
            
            if r and len(r) > 1:
                new = list(filter(lambda z: z != x, r))
                return [x, new[0]]