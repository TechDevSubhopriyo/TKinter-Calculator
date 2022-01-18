OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_to_postfix(expression):
    stack = []
    output = list()
    for ch in expression:
        if ch not in OPERATORS:
            output.append(ch)
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return output

