
def my_decorator(func):  #receives the function as an argument
    def wrapper():  #the wrapper function will be called instead of the original function which is modified version of function
        print("something is happening before the function is called.")
        func()
        print("something is happening after the function is called.")
    return wrapper #return the wrapper function

#applying decorators manually

def greet():
    print("hello")

greet=my_decorator(greet) #greet is now the wrapper function returned by my_decorator
greet() #calling the decorated function

