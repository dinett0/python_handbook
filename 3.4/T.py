import itertools


def rpn_translation(expression):
    def preced(op):
        lookup = {"~": 0, "->": 1, "^": 2, "or": 3, "and": 4, "not": 5, "(": -1}
        return lookup[op]

    ans = []
    operators = []
    for token in expression.replace("(", "( ").replace(")", " )").split():
        if token in "ABC":
            ans.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                ans.append(operators.pop())
            operators.pop()
        else:
            while operators and (
                preced(operators[-1]) > preced(token)
                or preced(operators[-1]) == preced(token)
            ):
                ans.append(operators.pop())
            operators.append(token)

    for operator in operators[::-1]:
        ans.append(operator)

    return " ".join(ans)


def evaluate(rpn_expr, a, b, c):
    rpn_expr = rpn_expr.replace("A", str(a)).replace("B", str(b)).replace("C", str(c))
    stack = []
    for token in rpn_expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            if token == "not":
                stack.append(not stack.pop())
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                match token:
                    case "~":
                        res = (not op1 or op2) and (not op2 or op1)
                    case "^":
                        res = (not op2 and op1) or (not op1 and op2)
                    case "->":
                        res = not op1 or op2
                    case "or":
                        res = op1 or op2
                    case "and":
                        res = op1 and op2
                stack.append(res)
    return int(stack[0])


expression = rpn_translation(input())
# print(expression)
print("A B C F")
for a, b, c in itertools.product([0, 1], repeat=3):
    print(a, b, c, evaluate(expression, a, b, c))
