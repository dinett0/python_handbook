ans = {}
while (pair := input().split()) != []:
    ans[pair[0]] = ans.get(pair[0], set()) | {pair[1]}
    ans[pair[1]] = ans.get(pair[1], set()) | {pair[0]}

for key in sorted(ans.keys()):
    ans_string = key + ": "
    s = set()
    for value in ans[key]:
        s |= ans[value] ^ {key}
    s -= ans[key]
    for i in sorted(s):
        ans_string += f"{i}, "
    print(ans_string.rstrip(", "))
