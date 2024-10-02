def validate_decorator(func):
    def wrapper(x):
        if x < 0:
            print("Invalid input")
            return
        return func(x)

    return wrapper


@validate_decorator
def square(x):
    return x * x


print(square(4)) 
print(square(-1))  
