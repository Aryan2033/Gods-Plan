def log_decorator(func):
    def wrapper():
        print(f"starting {func.__name__} function:")
        func()
        print(f"ending {func.__name__} function:")
    return wrapper 


@log_decorator
def say_hello():
    print("hello aryan")

say_hello()

@log_decorator
def train_model():
    print("training model...")
    # Simulate training process
    for i in range(5):
        print(f"Epoch {i+1}/5")
    print("Training completed.")

 #decorating the train_model function
train_model()