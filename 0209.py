class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        if max(nums) >= target:
            return 1
        
        queue = deque([])
        min_ = float('inf')
        
        for i in range(len(nums)):
            queue.append(nums[i])
            
            while sum(queue) >= target:
                if len(queue) < min_:
                    min_ = len(queue)
                queue.popleft()
                
        return min_ if min_ != float('inf') else 0