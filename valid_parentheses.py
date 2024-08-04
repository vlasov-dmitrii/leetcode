s = "()[]{}"
s = "(]"
s = ")()"
s = "["

def isValid(s):
    open = "[{("
    close = "]})"
    stack = []

    for char in s:
        if char in open:
            stack.append(char)
        
        else:
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{'):
                return False
            stack.pop()

    return not stack

print(isValid(s))


