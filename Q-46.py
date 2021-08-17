class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                result.append(perm + [n])

            nums.append(n)

        return result
