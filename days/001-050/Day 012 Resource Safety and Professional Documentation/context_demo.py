
with open("file.txt", "w") as f:
    f.write("hello aryan")
# The above code will automatically close the file after the block is executed, even if an error occurs.

print("file is automatically closed after the block is executed.")


with open("file.txt","r") as fi:
    content=fi.read()
    print(content)

          
    