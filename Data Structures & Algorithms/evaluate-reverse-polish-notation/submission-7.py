class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token=="*":
                stack.append(stack.pop()*stack.pop())
            elif token=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif token=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(float(b/a)))
            else:
                # must be an int
                stack.append(int(token))
        
        return stack[0]