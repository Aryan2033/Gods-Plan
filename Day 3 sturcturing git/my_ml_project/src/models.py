class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    def train(self, X, y):
        self.X = X
        self.y = y
        print(f"Training the neural network with the provided data...{self.X} and {self.y}")

    def predict(self, X):
        print("Making predictions with the trained neural network...")

    def evaluate(self,x,y):
        raise NotImplementedError("SUbsclasses must implement this method")
       
class DecisionTree(NeuralNetwork):
    def __init__(self,max_depth):
        super().__init__(layers=4)
        self.max_depth = max_depth
        print(f"Initialized Decision Tree with max depth of {self.max_depth} with layers {self.layers}")

    def evaluate(self, x, y):
        self.x = x
        self.y = y
        print("Evaluating the decision tree model...")

S1=NeuralNetwork([64, 32, 16])
S2=DecisionTree(max_depth=5)
print(S1.layers,S2.layers)
print(S2.train(2,3))
S2.evaluate(2,3)