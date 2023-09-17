def secret_replace(text, **replace_pat):
    result = []
    replace_pat = {key: [value, 0] for key, value in replace_pat.items()}
    for char in text:
        if char in replace_pat:
            pointer = replace_pat[char][1]
            result += replace_pat[char][0][pointer]
            replace_pat[char][1] = (pointer + 1) % len(replace_pat[char][0])
        else:
            result += char
    return "".join(result)


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)

print(result)
