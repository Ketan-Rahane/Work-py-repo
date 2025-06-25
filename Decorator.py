# Define the decorator
def log_subtract(func):
    def wrapper(a, b):
        print("Subtracting the values")
        return func(a, b) 
    return wrapper

@log_subtract
def subtract(a, b):
    return a - b

# Calling the function
result = subtract(10, 4)
print("Result:", result)
