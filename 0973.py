class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        
        for point in points:
            distance = sqrt((point[0]**2) + (point[1]**2))
            results.append([distance, point])
            
        results.sort()
        
        return [res[1] for res in results[:k]]