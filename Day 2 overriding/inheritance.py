class BaseModel:
    def train(self,data):
        print("Training the base model...")

    def predict(self,data):
        print("Predicting with the base model..." )

    def save(self,path):
        print(f"saving model to {path}...")

class RandoForest(BaseModel): # This class inherits from BaseModel
    pass                      # This means RandoForest has all the methods of       BaseModel without needing to redefine them such as train, predict, and save.


model=RandoForest() 
model.train("data")
model.predict("data")
model.save("model.plk")




