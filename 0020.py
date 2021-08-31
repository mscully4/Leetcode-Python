class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        brackets = {
            "(": ")", "{": "}", "[": "]"
        }
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif brackets[stack.pop()] != s[i]:
                    return False
                
        return True if not stack else False