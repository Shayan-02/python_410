def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_decorator(5)
def greet():
    print("Hello!")


greet()
