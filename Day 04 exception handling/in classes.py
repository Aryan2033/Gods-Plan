class maths:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def divide(self):
        if self.b==0:
            raise ValueError("cannot divide by zero")
        else:
            return self.a/self.b
        
s1=maths(10,2)
print(s1.divide())

# //this is traditional method of handling exception but we can also use try except block to handle exception in a better way as shown in the below code


try:
    s2=maths(10,0)
    s2.divide()
except ValueError as e:
    print(e)



#real world example of handling exception using try except block

class dataloader:

    def __init__(self,filename):
        self.filename=filename

    def load_data(self):
        try:
            with open(self.filename,"r") as file:
                content=file.read()

        except FileNotFoundError:
            print("file not found")

        finally:
            print("execution is finished")

data=dataloader("data.txt")
data.load_data()

# in the above code we are trying to open a file that does not exist and we are handling the exception using try except block and finally block is used to print a message after the execution is finished.




