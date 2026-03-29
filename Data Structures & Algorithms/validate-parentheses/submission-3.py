class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        pairs={
            "}":"{",
            ")":"(",
            "]":"["
        }

        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
            else:
                if len(stack)>0 and pairs[bracket]==stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack)>0:
            return False
        return True