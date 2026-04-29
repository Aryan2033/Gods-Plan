from src.models import DecisionTree
from src.processing import Data_cleaner

if __name__=="__main__":
    print("Welcome to my machine learning project!")

cleaner=Data_cleaner("raw_data.csv")
print("cleaner ready to use")

model=DecisionTree(max_depth=5)
print("model ready to use")