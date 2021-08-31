class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memory = {
            "(": n, 
            ")": n
        }
        
        answers = set()
    
        def recurse(string, memory, answers):
            # print(string, memory)
            if len(string) == n * 2:
                if self.is_valid(string):
                    answers.add(string)
            
            elif len(string) < n * 2:
                left_counter = memory["("] 

                if left_counter > 0:
                    recurse(string + "(", {"(": memory["("] - 1, ")": memory[")"]}, answers)
                    
                right_counter = memory[")"] 
                if right_counter > 0:
                    recurse(string + ")", {")": memory[")"] - 1, "(": memory["("]}, answers)

        recurse("", memory, answers)
        return answers
    
    def is_valid(self, string):
        if len(string) % 2 != 0:
            return False
        
        stack = []
        
        for i in range(len(string)):
            if string[i] == "(":
                stack.append(string[i])
            else:
                if not stack:
                    return False
                elif stack.pop() != "(":
                    return False
                
        return True if not stack else False