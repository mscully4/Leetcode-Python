class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_length = 0
        longest = ''
        
        for i in range(len(s)):
            b, f = i, i
            
            while b >= 0 and f < len(s) and s[b] == s[f]:
                if f - b + 1 > longest_length:
                    longest = s[b:f+1]
                    longest_length = f - b + 1
                
                f += 1
                b -= 1
                

            b, f = i, i+1
            while b >= 0 and f < len(s) and s[b] == s[f]:
                if f - b + 1 > longest_length:
                    longest = s[b:f+1]
                    longest_length = f - b + 1
                
                f += 1
                b -= 1       
                
        return longest