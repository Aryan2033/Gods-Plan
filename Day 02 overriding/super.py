class person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        print(f"person {self.name} is created")

class student(person):
    def __init__(self,name:str,grade:str):
        super().__init__(name,age=20)# This line calls the __init__ method of the parent class (person) using super(). It allows us to initialize the name and age attributes of the person class while still providing the grade attribute specific to the student class.
        self.grade=grade
        print(f"student {self.name} having grade {self.grade}")

student1=student("alice","A")
print(student1.name,student1.age,student1.grade)


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)   # direct parent call: you must pass self
        #Here Person.__init__ is being called like a normal function, so it needs both arguments: self (the current Student object) ,name