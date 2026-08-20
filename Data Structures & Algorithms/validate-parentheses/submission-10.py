class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack: list[str] = []

        for bracket in s:
            if bracket in pairs.keys(): # this is a closing bracket
                if (
                    stack 
                    and pairs[bracket] == stack[-1]
                ):
                    stack.pop() # this is a match, remove from stack
                else:
                    return False
            else:
                stack.append(bracket)

        return False if stack else True