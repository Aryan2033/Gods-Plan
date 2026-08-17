try:
    num=int(input("Enter a number: "))
    result=10/num
   
except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

else:
   print(f"the reuslt of 10 divoded by {num} is {result}") 



class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def divide(self):
        try:
            result=self.a/self.b
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        

c1=calc(10,0)
print(c1.divide())