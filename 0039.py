class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations=set()
        candidates.sort()
        
        def recurse(arr, j):
          
            for i in range(j, len(candidates)):
                sum_of_array = sum(arr)
                if sum_of_array == target:
                    combinations.add(tuple(arr))
                    return
                elif sum_of_array + candidates[i] > target:
                    return
                recurse(arr+[candidates[i]], i)
                
        recurse([], 0)
        return combinations