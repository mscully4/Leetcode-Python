class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        ptr = n - 2
        while ptr >= 0 and nums[ptr] >= nums[ptr+1]:
            ptr -= 1       
            
        for i in range(n-1,ptr,-1):
            if nums[ptr] < nums[i]:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                break
                
        nums[ptr+1:] = sorted(nums[ptr+1:])