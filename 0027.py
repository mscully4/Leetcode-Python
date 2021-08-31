class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        initial_length = len(nums)
        occurences = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
                occurences += 1
                
        nums.sort()
                
        return initial_length - occurences