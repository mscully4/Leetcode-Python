class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_p = "".join(sorted(p))
        
        start = 0
        end = len(p)
        results = []
        mem = {}
        
        while end <= len(s):
            if mem.get(s[start:end], False) or "".join(sorted(s[start:end])) == sorted_p:
                mem[s[start:end]] = True
                results.append(start)
            else:
                mem[s[start:end]] = False
                
                
            start += 1
            end += 1
            
        return results
                