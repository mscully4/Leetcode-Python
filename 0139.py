class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()
        
        
        def dfs(string):
            if string in seen:
                return False
            
            for key in wordDict:
                if key == string:
                    print(key, string)
                    return True
                elif self.safe_index(string, key, 0):
                    if dfs(string[len(key):]):
                        return True
            
            seen.add(string)

        return dfs(s)
    
    def safe_index(self, string, substring, index):
        try:
            return string.index(substring) == index
        except:
            return False