expression = input()
stack = []
for i in expression.split():
    if i.isdigit():
        stack.append(int(i))
    elif i == "@":
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        stack.append(b)
        stack.append(a)
        stack.append(c)
    elif i in "+-*/":
        b = stack.pop()  # right parameter
        a = stack.pop()  # left parameter
        match i:
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "*":
                stack.append(a * b)
            case "/":
                stack.append(a // b)
    else:
        a = stack.pop()
        match i:
            case "~":
                stack.append(a * -1)
            case "!":
                for factor in range(1, a):
                    a *= factor
                stack.append(a)
            case "#":
                stack.append(a)
                stack.append(a)
    # print(stack)

print(stack[0])
