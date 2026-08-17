try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")

print("execution is finished:")

