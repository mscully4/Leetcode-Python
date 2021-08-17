class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        f = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        results = []
        
        if len(digits) > 0:
            index = 1
            for c in f[int(digits[0])]:
                results.extend(self.combos(c, index, digits, f))
        return results
            
            
    def combos(self, c, index, digits, f):
        if len(c) == len(digits):
            return [c]
        
        l = []
        for b in f[int(digits[index])]:
            t = self.combos(c + b, index+1, digits, f)
            l.extend(t)
        return l
        