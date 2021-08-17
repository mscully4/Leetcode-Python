class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'["!?\',;.]', ' ', paragraph)
        
        mem = {}
        for word in paragraph.split(' '):
            word = word.lower().strip()
            if word not in banned and word != '':
                res = mem.get(word, 0)
                mem[word] = res + 1
         
        max_count = 0
        max_word = ''
        for k, v in mem.items():
            if v > max_count:
                max_word = k
                max_count = v
                
        return max_word