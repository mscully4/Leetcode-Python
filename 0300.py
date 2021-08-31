class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = []
        for i in nums:
            if not m or m[-1] < i:
                m.append(i)
            else:
                m[bisect_left(m,i)] = i
 
        return len(m)