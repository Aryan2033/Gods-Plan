# class BaseModel:
#     def predict(self,data):
#         raise NotImplementedError("Subclasses must implement this method") 
#     # This method is defined in the BaseModel class but raises a NotImplementedError. This means that any subclass of BaseModel must provide its own implementation of the predict method, otherwise it will raise an error when called. This is a way to enforce that certain methods must be implemented by subclasses, ensuring that they adhere to a specific interface or contract.
    
# class RandomForest(BaseModel):
#     pass

# # model=RandomForest()
# # model.predict("data")


# #in real syytem

class System:
    def __init__(self,name):
        self.name=name
        print(f"System initialized: {self.name}")

    def Start(self, data):
        raise NotImplementedError("Subclasses must implement this method")
    def Train(self, data):
        raise NotImplementedError("Subclasses must implement this method")
    
class Model(System):
    
    
    def Start(self,data):
        self.data=data
        print(f"Starting the model with {self.data}")

    def Train(self,data):
        self.data=data
        print(f"Training the model with {self.data}")


# run=Model()
# run.Start("parameters")
# run.Train("training data")


class NeuralNetwork(System):
    def Start(self, data):
        print(f"Starting Neural Network with {data}")
    
    def Train(self, data):
        print("Training Neural Network using backpropagation")

model=[Model("engine"), NeuralNetwork("Neural Network")]
for m in model:
    m.Start("initialization data")
    m.Train("testing data")