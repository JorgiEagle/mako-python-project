import pandas as pd
import numpy as np
# Mako 2022 Virtual Internship python project
def print_output(symbol, max_price, min_price, average_price, total_volume):
    """Prints formatted output of aggregates for given symbol."""
    print(f'Symbol: {symbol}, Max Price: {max_price:4}, Min Price: {min_price:4}, '\
            f'Average Price: {average_price:7.2f}, Total Volume: {total_volume:5}')

def calc_aggregates(df):
    return df["Price"].max(), df["Price"].min(), df["Price"].mean(), df["Volume"].sum()


def main():
    input_file = 'https://storage.googleapis.com/temp-bucket-5862/input_data.csv'
    input_headers = ["Timestamp", "Symbol", "Volume", "Price"]
    #load into a data frame
    trades_df = pd.read_csv(input_file, names=input_headers)
   
    unique_symbols = np.sort(trades_df["Symbol"].unique())
    for entry in unique_symbols:
        print_output(entry, *calc_aggregates(trades_df[trades_df.Symbol == entry]))
    

if __name__ == "__main__":
    file2 = "./input.csv"
    file = 'https://storage.googleapis.com/temp-bucket-5862/input_data.csv'
    main()
