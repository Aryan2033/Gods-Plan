def read_number():
    while True:        # we are using while loop to keep asking the user for input until they enter a valid number
        try:
            num=int(input("enter a number:"))
            return num
        except ValueError:
            print("invalid input please enter a number")#we used print statement to inform the user that they have entered an invalid input and to enter a valid number.if we have used raise or return statement here then the function would have returned and the user would not have been able to enter a valid number. but by using print statement we are able to keep asking the user for input until they enter a valid number.

number=read_number()
print(f"you entered: {number}")