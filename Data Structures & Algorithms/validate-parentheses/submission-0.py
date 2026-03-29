class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs={
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack=[]
        for b in s:
            if b in pairs and len(stack)>0 and stack[-1]==pairs[b]:
                stack.pop()
            else:
                stack.append(b)
        
        if len(stack)>0:
            return False
        return True