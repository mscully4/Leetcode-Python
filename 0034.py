class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]

        results = []
        position = 0
        
        
        def binarySearch(lst, position, results):
            if len(lst) == 1:
                if lst[0] == target:
                    results.append(position)
                return
            
            half = int(len(lst) / 2)
            
            a = lst[:half]
            b = lst[half:]
            
            binarySearch(a, position, results)
            binarySearch(b, position + half, results)
            
            
        binarySearch(nums, position, results)
        return [min(results), max(results)] if len(results) > 0 else [-1, -1]


solution = Solution().searchRange([], 0)
print(solution)