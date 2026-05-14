class Solution:
    def isValid(self, s: str) -> bool:
        pairs: dict = {
            "]":"[",
            "}": "{",
            ")":"("
        }
        stack=[]

        for b in s:
            if b not in pairs:
                stack.append(b)
            else:
                if stack and stack[-1]==pairs[b]:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True