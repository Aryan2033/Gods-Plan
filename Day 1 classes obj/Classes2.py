class System:
    def __init__(self, model_name):
        self.model_name = model_name

    def prediction(self, data):
        print(f"the model {self.model_name} is making prediction on {data}")

s2 = System("local model")

print("1) Class object:", System)
print("2) Class type:", type(System))
print("3) Instance object:", s2)
print("4) Instance type:", type(s2))

print("5) Class namespace keys:", [k for k in System.__dict__.keys() if not k.startswith("__")])
print("6) Instance namespace:", s2.__dict__)

print("7) Raw function from class:", System.__dict__["prediction"])
print("8) Bound method from instance:", s2.prediction)
print("9) Bound method __self__:", s2.prediction.__self__)
print("10) Bound method __func__:", s2.prediction.__func__)

s2.prediction("Methods to solve habits.png")

# So:

# Class dictionary: stores shared things like methods.
# Instance dictionary: stores per-object values like name, age, model_name.

# What each part proves:

# System is a class object
# Python classes are also objects.
# So type(System) is usually class type.

# s2 is an instance
# type(s2) points back to System.

# Where data is stored
# s2.dict holds instance attributes, so you will see:
# model_name: local model

# Where methods are stored
# prediction lives in the class dictionary, not inside instance dictionary.

# Why s2.prediction works
# When you access prediction from s2, Python creates a bound method:

# self is s2
# func is original function in class