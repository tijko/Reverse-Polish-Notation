import sys

def RPN(equation):
    ops = {'(':1, '-':2, '+':2, '*':3, '/':3}
    stack = []
    out = []
    for token in equation:
        if token.isdigit():
            out.append(token)
        else:
            if (len(stack) == 1 and 
                token in ops and 
                ops[token] <= ops[stack[-1]] and 
                token != '('):
                out.append(stack[-1])
                stack.pop(-1)
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif len(stack) == 1 and token in ops and ops[token] >= ops[stack[-1]]:
                stack.append(token)
            elif len(stack) > 1 and token in ops and ops[token] < ops[stack[-1]]:
                out.append(stack[-1])
                stack.pop(-1)
                out.append(stack[-1])
                stack.pop(-1)
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(':
                    out.append(stack[-1])
                    stack.pop(-1)
                stack.pop(-1)
            elif (len(stack) > 1 and 
                  token in ops and 
                  ops[token] >= ops[stack[-1]] and 
                  stack[-1] != '('):
                out.append(stack[-1])
                stack.pop(-1)
                stack.append(token)
            elif len(stack) > 1 and stack[-1] == '(' and token in ops:
                stack.append(token)
            elif len(stack) < 1 and token in ops:
                stack.append(token)
    if len(stack) > 0:
        sorted(stack, key=ops.get)
        stack = stack[::-1]
        for token in stack:
            out.append(token)
    fin = ''
    for i in out:
        fin += ' ' + i
    print fin


if __name__ == '__main__':
    try:
        data = sys.argv[1]
        RPN(data)
    except IndexError:
        print 'No input was given.'
