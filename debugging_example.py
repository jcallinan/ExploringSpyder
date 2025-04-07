

def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.  This version has a bug!
    """
    sum_so_far = 0  # Changed from sum to sum_so_far
    for number in numbers:
        sum_so_far += number
    return sum_so_far

def main():
    """
    Main function to demonstrate the calculate_sum function with a bug.
    """
    data = [1, 2, 3, 4, 5]
    expected_sum = sum(data) # Use the built-in sum() for comparison
    actual_sum = calculate_sum(data)

    print(f"Data: {data}")
    print(f"Expected Sum: {expected_sum}")
    print(f"Actual Sum: {actual_sum}")

    if actual_sum != expected_sum:
        print("Error: The calculate_sum function has a bug!")
    else:
        print("The calculate_sum function works correctly.")

if __name__ == "__main__":
    main()

