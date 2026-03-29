class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack=[]
        for b in s:
            if b not in pairs:
                # must be opening, add to stack
                stack.append(b)
            else: #must be closing, look for match
                # check if stack is non empty
                if not stack:
                    return False
                # check if last element is match
                if stack[-1]==pairs[b]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else: 
            return True