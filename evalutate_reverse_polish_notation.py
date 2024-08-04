
tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif token == '-':
            second = int(stack.pop())
            first = int(stack.pop())
            stack.append(first - second)
        elif token == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif token == '/':
            second = int(stack.pop())
            first = int(stack.pop())
            stack.append(first / second)
        else: # number
            stack.append(token)
    return int(stack[-1])

print(evalRPN(tokens))

 