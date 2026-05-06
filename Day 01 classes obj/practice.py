class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    
    def drive(self):
        print(f"{self.brand} {self.model} is moving at {self.speed} km/h")

s1=Car("Porsche",911,250)
s1.drive()


class Ram:
    def __init__(self,size,speed):
        self.size=size
        self.speed=speed

s2=Ram(16,300)
print(s2.size,s2.speed )


class Calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2

    def add(self):
        return self.number1+self.number2
    
    def substract(self):
        return self.number1-self.number2
    
    def multiply(self):
        return self.number1*self.number2
    
    def divide(self):
        if self.number2!=0:
          return self.number1/self.number2
        else:
            return "Error: Division by zero is not allowed."
        
    def optimal_divide(self):
        if self.number2==0:
            raise ValueError("Error: Division by zero is not allowed.")
        return self.number1/self.number2
        
calc=Calculator(10,0)
print("addition:",calc.add())
print("divide:" ,calc.divide())