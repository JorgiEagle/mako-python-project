import pandas as pd
import numpy as np
# Mako 2022 Virtual Internship python project
def print_output(symbol, max_price, min_price, average_price, total_volume):
    """Prints formatted output of aggregates for given symbol."""
    with open("function_output.txt", "a") as output:
        output.write(f'Symbol: {symbol}, Max Price: {max_price:4}, Min Price: {min_price:4}, '\
            f'Average Price: {average_price:7.2f}, Total Volume: {total_volume:5}\n')

def main():
    with open("function_output.txt", "w") as output:
        output.write("Timings\n")
    input_file = 'https://storage.googleapis.com/temp-bucket-5862/input_data.csv'
    input_headers = ["Timestamp", "Symbol", "Volume", "Price"]
    #load into a data frame
    trades_df = pd.read_csv(input_file, names=input_headers).groupby('Symbol')

    for name, group in trades_df:
        print_output(name, group['Price'].max(), group['Price'].min(), group['Price'].mean(), group['Volume'].sum())

    

if __name__ == "__main__":
    file2 = "./input.csv"
    file = 'https://storage.googleapis.com/temp-bucket-5862/input_data.csv'
    main()
