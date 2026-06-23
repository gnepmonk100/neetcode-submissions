class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        stack.append(tokens[0])
        stack.append(tokens[1])

        for idx in range(2, len(tokens)):
            if tokens[idx] in operators:
                if tokens[idx] == '+':
                    sum_tokens = int(stack[0]) + int(stack[1])
                    stack.pop()
                    stack.pop()
                    stack.append(sum_tokens)
                elif tokens[idx] == '-':
                    diff_tokens = int(stack[0]) - int(stack[1])
                    stack.pop()
                    stack.pop()
                    stack.append(diff_tokens)
                elif tokens[idx] == '*':
                    prod_tokens = int(stack[0]) * int(stack[1])
                    stack.pop()
                    stack.pop()
                    stack.append(prod_tokens)
                else:
                    quot_tokens = int(stack[0]) / int(stack[1])
                    stack.pop()
                    stack.pop()
                    stack.append(quot_tokens)
            else:
                stack.append(tokens[idx])
        return stack[0]



        


        