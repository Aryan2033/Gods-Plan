import logging

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(message)s-%(levelname)s"
)

def debug_log(func):
    def wrapper(*args, **kwargs):
        
        logging.debug(f"Excecuting function: {func.__name__} with arguments {args} and keyword arguments {kwargs}")

        result=func(*args, **kwargs)
        logging.debug(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

