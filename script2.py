import numpy as np
import pandas as pd

def analyze_data():
    """
    This function demonstrates some basic data analysis using NumPy and Pandas.
    """
    # Create a NumPy array
    data = np.array([1, 2, 3, 4, 5])
    mean_value = np.mean(data)
    print(f"NumPy Array: {data}")
    print(f"Mean: {mean_value}")

    # Create a Pandas Series
    s = pd.Series([10, 20, 30, 40, 50], name="MyData")
    print(s)

    # Create a Pandas DataFrame
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6],
        'col3': [7, 8, 9]
    })
    print(df)
    print(df.describe())

def main():
    analyze_data()

if __name__ == "__main__":
    main()
