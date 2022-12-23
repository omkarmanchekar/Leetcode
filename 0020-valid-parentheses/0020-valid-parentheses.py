class Solution:
    def isValid(self, s: str) -> bool:
        
        stack  = []
        hash = {"(":")","{":"}","[":"]"}
        
        def validClosingBracket():
            return hash[stack[-1]]
        
        
        for i in s:
            if(i in hash):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                else:
                    if(i == validClosingBracket()):
                        stack.pop()
                    else:
                        return False
                    
        if(len(stack) == 0):
            return True 
        else:
            return False