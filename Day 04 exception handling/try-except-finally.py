# try:
#     result = 10 / 0

# except ZeroDivisionError:
#     print("cannot divide by zero")




try:
    num=int(input("enter a number:"))
    result=10/num

except ValueError:
    print("invalid input please enter a number")

except ZeroDivisionError:
    print("cannot divide by zero")

finally:
    print("execution is finished")

    

