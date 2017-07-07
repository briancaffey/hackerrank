def is_matched(expression):
    o = ['(', '[', '{']
    c = [')', ']', '}']
    stack = []
    for num, b in enumerate(expression):
        if b in o:
            stack.append(b)
        else:
            if len(stack)==0:
                return False
            if b == ')':
                if stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    return False
            elif b == '}':
                if stack[-1] == '{':
                    stack = stack[:-1]
                else:
                    return False
            elif b == ']':
                if stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
