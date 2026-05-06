#class is bluprint to create objects
#class=design and object = real thing creaated from that design

class student1:
    pass
#pass is used to create empty class

S2=student1()
print(S2)


#s1 is object of class student
#without classes, small scripts are fine, but medium/large projects become harder to organize, reuse, debug, and extend.

class className:
    def __init__(self,parameters):
        #initialize the data

        def method(self):
            pass
        #behaviour
        #method is a function defined inside a class, and it describes the behavior of the objects created from that class.
#__init__ is a special method in Python classes, known as the constructor. It is automatically called when a new object of the class is created. The purpose of __init__ is to initialize the attributes of the object with the values provided as parameters.

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        #these are the attributes(data) of the class student, and they are initialized using the __init__ method. The self parameter refers to the instance of the class being created, allowing us to assign values to the attributes for each specific object.


    def intrudcution(self):
        print(f"my name is {self.name} and my age is {self.age}")


    def greet(self):
        print("Hello, I am AI engineer")  
            #this is method which is function defined inside the class student, and it describes the behavior of the objects created from that class. In this case, the greet method will print a greeting message when called on an instance of the student class.

S1=student("Aryan",23) #each object has its own memory 
print(S1.name,S1.age)
S1.greet()
S1.intrudcution()


class System:
    def __init__(self,model_name):
        self.model_name=model_name

    def prediction(self,data):
        print(f"the model {self.model_name} is making prediction on {data}")

s2=system("local model")
s2.prediction("Methods to solve habits.png")#It finds function prediction in class. Python binds that function to s2, creating a bound method.

#You only wrote one argument "local model"self is passed automatically by Python as the new instance.


    