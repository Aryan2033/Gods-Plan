class BaseModel:
    def train(self,data):
        print("Training the base model...")

    def predict(self,data):
        print("Predicting with the base model..." )

    def save(self,path):
        print(f"saving model to {path}...")

class RandomForest(BaseModel): 
    def train(self,data):
        print("Training the Random Forest model... ") # This method overrides the train method of the BaseModel class. When we call the train method on an instance of RandoForest, it will execute this overridden method instead of the one in BaseModel.
        #Even though BaseModel has train(), child version replaces it


class NeuralNetwork(BaseModel):
    def predict(self,data):
        print("Predicting with the Neural Network model...") # This method overrides the predict method of the BaseModel class. When we call the predict method on an instance of NeuralNetwork, it will execute this overridden method instead of the one in BaseModel.


# super() (Connecting Parent + Child)

# Sometimes you want both:

# base behavior
# extra child behavior

class Knn(BaseModel):
    def train(self,data):
        super().train(data)
        print("Training the KNN model...") # This method overrides the train method of the BaseModel class, but it also calls the original train method from BaseModel using super(). This allows us to retain the base behavior while adding extra child behavior specific to KNN.





model=RandomForest() 
model.train("data")
model.predict("data")
model.save("model.plk")
nn_model=NeuralNetwork()
nn_model.train("data")
nn_model.predict("data")
Knn_model=Knn()
Knn_model.train("data")







