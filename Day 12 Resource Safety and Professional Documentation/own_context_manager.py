


class sensor:

    def __enter__(self):
        print("entering into sensor")

        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        print("exiting from sensor")

    def read(self):
        print("reading data from sensor")


#using the context manager

with sensor() as s:
    s.read()
    x = 1 / 0  
    print("doing some processing with the sensor data")

# even if error occurs, the __exit__ method will be called to ensure proper cleanup of resources.