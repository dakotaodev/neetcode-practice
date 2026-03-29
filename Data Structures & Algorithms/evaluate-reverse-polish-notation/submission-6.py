class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        for token in tokens:
            if token == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1+v2)
            elif token == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2-v1)
            elif token == "*":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1*v2)
            elif token == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(float(v2)/v1))
            else:
                stack.append(int(token))

        return stack[0]