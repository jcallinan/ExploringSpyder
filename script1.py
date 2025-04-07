# contents of: examples/script1.py
def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}!")

def add_numbers(x, y):
    """
    This function adds two numbers and returns the result.
    """
    sum_result = x + y
    return sum_result

# Main part of the script
if __name__ == "__main__":
    user_name = "Alice"
    greet(user_name)

    num1 = 10
    num2 = 5
    addition_result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {addition_result}")

    # Example list
    my_list = [1, 2, 3, 4, 5]
    print(f"My list: {my_list}")

    # Example dictionary
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(f"My dictionary: {my_dict}")
