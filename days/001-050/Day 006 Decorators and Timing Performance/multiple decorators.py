import time
from functools import wraps

def log_decorator(func):
    @wraps(func) #this is used to preserve the original function's metadata like name and docstring
    def wrapper(*args, **kwargs):
        print(f"starting {func.__name__} function:")
        result=func(*args, **kwargs)
        print(f"ending {func.__name__} function:")
        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        starrt = time.time()

        result1=func(*args, **kwargs)

        end= time.time()

        print(f"execution time: {end-starrt} seconds")

        return result1
    return wrapper


@log_decorator
@timer

def train_model(data,epochs):

    print("training model...")

    for i in range(epochs):
        print(f"epochs {i+1}/{epochs}")

    print("training completed.")

train_model("neural network",5)








