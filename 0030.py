class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        
        start = 0
        end = len(words) * len(words[0])
        
        results = []
        while end < len(s) + 1:
            if words == list(sorted([s[i:i+len(words[0])] for i in range(start, end, len(words[0]))])):
                results.append(start)
            
            start += 1
            end += 1
        
        return results