try:
    file=open("notes.txt")
    content=file.read()
    print(content)

except FileNotFoundError:
    print("file not found")
finally:
    print("execution is finished:")
    file.close()

