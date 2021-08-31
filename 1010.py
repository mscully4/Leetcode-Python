class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mem = {}
        
        for i, dur in enumerate(time):
            key = 60 - (dur % 60) if dur % 60 != 0 else 0
            r = mem.get(key, [])
            r.append(i)
            mem[key] = r
            
        used = set()
        pairs = 0
        for n in range(len(time)):
            r = mem.get(time[n] % 60, [])
            if time[n] % 30 != 0 and n not in used:
                pairs += len(r)
                used.update(r)
                
            if time[n] % 30 == 0 and n not in used:
                used.update(r)
                pairs += sum(range(1, len(r)))
                
        return pairs