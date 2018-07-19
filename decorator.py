from time import time
import logging
from functools import wraps

def timer(input_function):
    @wraps(input_function)
    def wrapper(*args, **kwargs):
        start = time()
        result_value = input_function(*args, **kwargs)
        end = time()
        print("Time elapsed", end - start)
        return result_value
    return wrapper

# timer function takes input_function(any function) as argument so input_function is first class function
# timer function accepts function as input and return function as output, so timer is higher order
# since wrapper has access to input even after completion of timer function , it is called closure.

def logger(input_function):
    logging.basicConfig(filename="decorator_logger.txt", level=logging.INFO)
    @wraps(input_function)
    def wrapper(*args, **kwargs):
        logging.info(f"function, {input_function.__name__} ran with arguents {args}: {input_function.__name__}{args}")
        return input_function(*args, **kwargs)
    return wrapper

@logger
@timer
def add(x, y):
    return x + y


print(add(1,2))








        