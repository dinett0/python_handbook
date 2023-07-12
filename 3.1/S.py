expression = input()
stack = []
for i in expression.split():
    if i.isdigit():
        stack.append(int(i))
    else:
        b = stack.pop()  # right parameter
        a = stack.pop()  # left parameter
        match i:
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "*":
                stack.append(a * b)
print(stack[0])
