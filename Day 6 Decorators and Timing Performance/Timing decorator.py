import time

def timer(func):
    def wrapper():

        start= time.time() #record the start time

        func()

        end= time.time() #record the end time   

        print(f"execution time: {end-start} seconds") #calculate and print the execution time
    return wrapper


@timer

def predict():
    print("predicting....")

    time.sleep(2) #simulate a time-consuming prediction process

predict()
#predicting....
#execution time: 2.0010669231414795 seconds
