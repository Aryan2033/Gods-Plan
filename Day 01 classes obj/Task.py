class Model:
    def __init__(self,name:str,version:float):
        self.name=name
        self.version=version

    def load_data(self,data):
        print(f"model {self.name} is loading data {data}")

    def predict(self,input_data):
        return input_data**2

m1=Model("My_model",1.0)
m1.load_data("data.csv")
result=m1.predict(5)
print("Prediction result:",result)



#2nd task

class SmartPredictor:
    def __init__(self, version: str):
        self.version = version
        print(f"System Online: Version {self.version}")

    def predict(self, x: int) -> int:
        return x * 2
    
    def evaluate(self,actual:int):
        return actual-self.predict(actual)

# Day 1 Test
model = SmartPredictor("1.0.0")
print(f"Result: ,{model.predict(10)}")
print(f"Evaluation: ,{model.evaluate(20)}")