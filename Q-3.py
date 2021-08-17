class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)

        start, end = 0, 0
        unique = set()
        max_length = 0

        while end < len(s):
            if s[end] not in unique:
                unique.add(s[end])
                end += 1
                max_length = max(max_length, len(unique))
            else:
                unique.remove(s[start])
                start += 1


        return max_length

       

if __name__ == "__main__":
    s = Solution()
    # r = s.lengthOfLongestSubstring("aab")
    # r = s.lengthOfLongestSubstring("abcabcbb")
    r = s.lengthOfLongestSubstring("pwwkew")
    print(r)