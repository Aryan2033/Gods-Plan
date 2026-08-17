from first_decorator import my_decorator

# Instead of:

# greet = my_decorator(greet)

#use the @ symbol to apply the decorator
@my_decorator
def greet():
    print("hello")

greet()
