"""
This script contains a function with a more complex bug, designed for debugging practice.
"""

def process_data(data):
    """
    Processes a list of numerical data.
    This version contains a bug!
    """
    results = []
    for i in range(len(data)):
        value = data[i]
        if value > 0:
            result = value * 2
        elif value < 0:
            result = value / 2
        #  Missing case: what if value is 0?
        results.append(result)  # Bug: result might not be defined

    return results

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average


def main():
    """
    Main function to demonstrate the process_data function with a bug
    and the calculate_average function.
    """
    test_data = [10, -5, 0, 20, -10, 5, 0, 15]
    print(f"Original Data: {test_data}")

    processed_results = process_data(test_data)
    print(f"Processed Data: {processed_results}")

    average_result = calculate_average(processed_results)
    print(f"Average of Processed Data: {average_result}")



if __name__ == "__main__":
    main()
