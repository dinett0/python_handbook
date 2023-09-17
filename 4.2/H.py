string = "Яндекс использует Python во многих проектах"
print(sorted(string.split(), key=lambda string: (len(string), string.lower())))
