from pydantic import BaseModel, Field, ValidationError # noqa: F401

#define data schema


class SensorData(BaseModel):
    machine_id:str
    temprature:float=Field(..., gt=-40, lt=125) #temperature range for industrial machines
    pressure:float=Field(..., gt=0) #pressure must be positive
    humidity:float=Field(..., ge=0, le=100) #humidity must be between 0 and 100

#valid data
try:
    valid_sensor= SensorData(
        machine_id="M123",
        temprature=85.5,
        pressure=1.2,
        humidity=45.0
    )
    print("Valid sensor data:", valid_sensor)

except ValidationError as e:
    print("Validation error for valid data:", e)


#invalid data
try:
    invalid_sensor=SensorData(
        machine_id="M124",
        temprature=150.0, #invalid temperature
        pressure=-1.0, #invalid pressure
        humidity=110.0 #invalid humidity
    )
    print("Invalid sensor data:", invalid_sensor)
except ValidationError as e:
    print("Validation error for invalid data:", e)




# output:
# Input should be less than 125 [type=less_than, input_value=150.0, input_type=float]
#     For further information visit https://errors.pydantic.dev/2.13/v/less_than
# pressure
#   Input should be greater than 0 [type=greater_than, input_value=-1.0, input_type=float]
#     For further information visit https://errors.pydantic.dev/2.13/v/greater_than
# humidity
#   Input should be less than or equal to 100 [type=less_than_equal, input_value=110.0, input_type=float]
#     For further information visit https://errors.pydantic.dev/2.13/v/less_than_equal