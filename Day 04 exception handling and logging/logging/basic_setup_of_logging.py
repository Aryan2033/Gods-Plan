import logging
# Set up basic logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"#set the format of the log messages
)


class calculator:
    def add(self,a,b):
        result=a+b
        logging.info(f"addition of {a} and {b} is {result}")
        return result
    
    def sub(self,a,b):
        result=a-b
        logging.info(f"substraction of {a} and {b} is {result}")
        return result
    
    def mul(self,a,b):
        result=a*b
        logging.info(f"multiplication of {a} and {b} is {result}")
        return result
    
    def div(self,a,b):
        if b==0:
            logging.error("division by zero is attempted")
            return "division by zero is not allowed"
        
        return a/b
    

# calc=calculator()
# calc.add(10,5)
# calc.sub(10,5)      
# calc.mul(10,5)
# calc.div(10,0)



# try :
#     re=10/0
# except ZeroDivisionError as e:
#     logging.error(f"an error occurred: {e}")

data=[1,2,3,None]

for d in data:
    if d is None:
        logging.warning("None value is encountered in the data list")
    else:
        logging.info(f"processing data: {d}")




