import logging
from Decorator_for_logging import debug_log

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(message)s-%(levelname)s"
)

class Base_model:
    def __init__(self, name):
        self.name = name

    def train(self, X, y):
        raise NotImplementedError("Subclasses must implement this method")



class neural_network(Base_model):
    def __init__(self, layers):
        super().__init__("Neural Network")
        self.layers = layers
    @debug_log
    def train(self, X, y):
        # Implementation for training the neural network
        self.X = X
        self.y = y
        logging.debug(f"Training the {self.name} with layers {self.layers}  on data X: {X} and y: {y}")

NN=neural_network([64, 32, 16])
NN.train(2,3)