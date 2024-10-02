import time


def time_calculator(func):
    def wrapper(*a, **b):
        start_time = time.time() 
        result = func(*a, **b)
        end_time = time.time() 
        execution_time = end_time - start_time  
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result

    return wrapper


@time_calculator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


result = example_function(1000000)
print(f"نتیجه تابع: {result}")

