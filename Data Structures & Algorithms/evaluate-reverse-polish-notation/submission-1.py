class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The top element is the SECOND operand
                b = stack.pop()
                # The next element down is the FIRST operand
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                # It's a number, convert to int and push to stack
                stack.append(int(token))
                
        return stack[0]