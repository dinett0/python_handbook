with open("file.txt", "r", encoding="UTF-8") as file_input:
    buffer = file_input.read()

for char in buffer:
    if ord(char) > 128:
        fetched_byte = bin(ord(char))[-8:]
        print(chr(int(fetched_byte, 2)), end="")
    else:
        print(char, end="")
