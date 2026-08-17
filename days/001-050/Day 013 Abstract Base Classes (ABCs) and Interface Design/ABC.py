from abc import ABC, abstractmethod

class BaseModel(ABC):
    
    @abstractmethod
    def train(self,X,y):
        pass

    @abstractmethod
    def predict(self,X):
        pass

# here base model is an abstract class and train and predict are abstract methods which means that any class that inherits from base model must implement these methods otherwise it will raise an error.

class LinearRegression(BaseModel):

    def train(self,X,y):
        # code to train the linear regression model
        print("Training the linear regression model with data X and labels y")
    def predict(self,X):
        # code to predict using the linear regression model
        print("Predicting using the linear regression model with data X")

# here linear regression class inherits from base model and implements the train and predict methods.

#error class

class DescisionTree(BaseModel):
    
    def train(self,X,y):
        # code to train the decision tree model
        print("Training the decision tree model with data X and labels y")
    # here we have not implemented the predict method which will raise an error when we try to create an object of the decision tree class.

s1=DescisionTree()
# this will raise an error because we have not implemented the predict method in the decision tree class.