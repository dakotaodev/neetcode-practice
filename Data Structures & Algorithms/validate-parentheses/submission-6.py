class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack=[]
        for bracket in s:
            if bracket not in pairs:
                # it is an opening
                stack.append(bracket)
            else:
                # closing. check if it closes
                if stack and pairs[bracket]==stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True