# Here we will begin my Python script for the Catan Picker

# Let's Begin Now

import csv

def readCSV():

    hexArray = []

    with open('catanBoard.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        line_count = 0
        for row in csv_reader:
            print(row)


def main():
    print("Hello World!")

    catanHexes = readCSV()

if __name__ == "__main__":
    main()
