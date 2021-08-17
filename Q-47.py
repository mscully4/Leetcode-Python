class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = self.permute(nums)
        return results
    
    def permute(self, nums):
        if len(nums) == 1:
            return [nums.copy()]
        
        used = {}
        used_nums = set()
        
        result = []
        for _ in range(len(nums)):
            x = nums[_]
            
            n = nums.pop(0)
            if not n in used_nums:
                perms = self.permute(nums)
                for perm in perms:
                    perm.append(n)
                    result.append(perm)

            used_nums.add(n)
            nums.append(n)
                

        return result
        