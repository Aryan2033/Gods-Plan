import time
def sensor_steam():

    sensor_id=1

    while True:

        temperature=20+sensor_id*0.5

        humidity=50+sensor_id*0.2

        yield{ #yield create dictonary with the current values of sensor_id, temperature and humidity without stopping the function, it will continue to generate new data when next is called
            "sensor_id": sensor_id,
            "temperature": temperature,
            "humidity": humidity
        }

        sensor_id+=1

stream= sensor_steam()
for _ in range(5):   

    data= next(stream)
    print(data)

    time.sleep(1)

# Generates one sensor reading
# Yields it
# Pauses at the yield line
# Waits for the next next() call
# Resumes and loops back to the top