# Here we will begin my Python script for the Catan Picker

# Let's Begin Now

import csv
from enum import Enum

class HexRes(Enum):
    Wood = "Wood"
    Brick = "Brick"
    Wheat = "Wheat"
    Sheep = "Sheep"
    Ore = "Ore"
    Desert = "Desert"

def readCSV():

    hexArray = []

    with open('catanBoard.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        line_count = 0
        for row in csv_reader:
            hexTuple = (row[0], row[1])
            hexArray.append(hexTuple)

        hexArray.pop(0)

    if verifyCSV(hexArray):
        return hexArray
    else:
        # throw error
        print("error has occured with the array")

    #print(hexArray)

def verifyCSV(hexArray):

    for tuple in hexArray:
        if( tuple[0] not in HexRes.__members__ ):
            print(tuple[0] + " is not a memeber")
            return False

        try:
            value = int(tuple[1])
        except ValueError:
            print("An item other than an Int was passed")

    return True


def main():
    print("Hello World!")

    catanHexes = readCSV()

if __name__ == "__main__":
    main()
