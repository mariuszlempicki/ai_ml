import time
from datetime import datetime

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas działania funkcji {func.__name__}: {round(end_time - start_time, 2)}s.")
        return result

    return wrapper


@measure_time
def print_numbers(x):
    for i in range(1, x+1):
        print(i)
        time.sleep(1)

print_numbers(5)

# =====

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as f:
            f.write(f"Function: {func.__name__} | Timestamp: {datetime.now()} | Args: {args}, {kwargs}\n")

        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(1, 2)

# =====
@measure_time
@log
def add(a, b):
    return a + b


# ======

def actual_rounding_decorator(param):
    def round_result(func):
        return lambda *args, **kwargs: round(func(*args, **kwargs), param)
    return round_result


@actual_rounding_decorator(3)
def calculate_average(a, b):
    return (a + b) / 2


calculate_average(1.242342, 2.23)