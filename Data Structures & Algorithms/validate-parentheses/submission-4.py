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
                stack.append(bracket)
            else:
                if stack and pairs[bracket]==stack[-1]:
                    stack.pop()
                else:
                    return False

        return False if stack else True