
class Solution:
    def numDecodings(self, s: str) -> int:
        mem = defaultdict(lambda: None)
        return self.recurse(s, mem)
    
    def recurse(self, string, memory):
        if len(string) == 0:
            return 1
        elif memory[string] != None:
            return memory[string]
        else:
            total = 0
            if string[0] != "0":
                total += self.recurse(string[1:], memory)
            if len(string) >= 2 and (string[0] == "1" or (string[0] == "2" and int(string[1]) <= 6)):
                total += self.recurse(string[2:], memory)
            memory[string] = total
            return total