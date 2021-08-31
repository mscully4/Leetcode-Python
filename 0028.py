class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 
        
        start = 0
        end = start + len(needle)
        
        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            
            start += 1
            end += 1
            
        return -1