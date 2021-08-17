class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mem = {}
        
        for i in range(len(s)):
            mem[s[i]] = i
                
        start = 0
        end = 1
        ma = 0
        
        result = []
        for i, c in enumerate(s):
            m = mem.get(c)
            if m > ma: ma = m

            if end > ma:
                result.append(end - start)
                start = i + 1
   
            end += 1
                
        return result