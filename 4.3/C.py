def make_equation(*coefficients, first_time=[True]):
    if len(coefficients) < 1:
        return ""
    if first_time[0]:
        string = ("(" * (len(coefficients) - 2)) + f"({coefficients[0]})"
        first_time[0] = False
    elif len(coefficients) < 2:
        string = f" * x + {coefficients[0]}"
    else:
        string = f" * x + {coefficients[0]})"
    return string + make_equation(*coefficients[1:])


# solve other variarnts

print(make_equation(3, 1))
