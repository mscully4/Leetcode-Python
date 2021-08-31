class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        
        for i in range(1, len(height)):
            left[i] = max(height[:i])
            
        for i in range(0, len(height) - 1):
            right[i] = max(height[i+1:])
            
        total = 0
        for j in range(len(height)):
            current = height[j] 
            min_ = min(left[j], right[j])
            if current <= min_:
                total += min_ - current
        
        return total