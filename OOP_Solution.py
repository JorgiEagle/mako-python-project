import requests
# An instrument class that represents the data for a single symbol
class Instrument:

    def __init__(self, name):
        self.name = name
        self.maxPrice = 0
        self.minPrice = 0
        self.totalPrice = 0
        self.tradeCount = 0
        self.totalVolume = 0

    def addTrade(self, volume, price):
        # Add the trade to the running totals
        self.totalVolume += volume
        self.totalPrice += price
        self.tradeCount += 1
        # Update max or min price if new price is better
        self.maxPrice = price if price > self.maxPrice else self.maxPrice
        # test for min price since given the safe assumption that price > 0 for all.
        self.minPrice = price if price < self.minPrice or self.minPrice == 0 else self.minPrice

    def printSummary(self):
        with open("oop_output.txt", "a") as output:
            output.write(f'Symbol: {self.name}, Max Price: {self.maxPrice:4}, Min Price: {self.minPrice:4}, '\
            f'Average Price: {self.totalPrice/self.tradeCount:7.2f}, Total Volume: {self.totalVolume:5}\n')
        # Example - print('Symbol: {} Max Price: {} Min Price: {} Average Price: {} Total Volume: {}'.format(self.name, self.maxPrice, self.minPrice, averagePrice, self.totalVolume))


def loadData(symbols, inputFile):
    # Open and read our input file
    res = requests.get(inputFile)
    file = res.iter_lines(decode_unicode=True)
    index = 0
    for line in file:
        # Split the CSV into it's components
        lineData = line.split(',')
        timestamp = int(lineData[0])
        symbol = lineData[1]
        volume = int(lineData[2])
        price = int(lineData[3])
        # if trade instrument not already in dictionary, initialize
        if symbol not in symbols:
            symbols[symbol] = Instrument(symbol)
        # update trade
        symbols[symbol].addTrade(volume, price)

def printSummary(symbols):
    # For each symbol (sorted alphabetically) print the summary
    for key in sorted(symbols):
        symbols[key].printSummary()

# Main code
def main():
    with open("oop_output.txt", "w") as output:
        output.write("Timings\n")
    # A dictionary to store our instrument information
    symbols = dict()
    inputFile = 'https://storage.googleapis.com/temp-bucket-5862/input_data.csv'
    loadData(symbols, inputFile)
    printSummary(symbols)

if __name__ == "__main__":
    main()