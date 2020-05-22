# Here we will begin my Python script for the Catan Picker

# Let's Begin Now

import csv
from hexCalc import HexCalculations
from enum import Enum

class HexRes(Enum):
    Wood = "Wood"
    Brick = "Brick"
    Wheat = "Wheat"
    Sheep = "Sheep"
    Ore = "Ore"
    Desert = "Desert"

def readCSV():

    hexResArr = []
    hexNumArr = []

    with open('catanBoard.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        line_count = 0

        for row in csv_reader:
            hexResArr.append(row[0].title())
            hexNumArr.append(row[1])

        hexResArr.pop(0)
        hexNumArr.pop(0)

    try:
        verifyResArr(hexResArr)
    except:
        print("Resources have an issue.")

    try:
        verifyNumArr(hexNumArr)
    except:
        print("Numbers have an issue.")


    #print(hexArray)

def verifyResArr(hexResArr):
    print("hexResArr")
    WoodCnt = 4
    BrickCnt = 3
    WheatCnt = 4
    SheepCnt = 4
    OreCnt = 3
    DesertCnt = 1

    for item in hexResArr:

        if( item not in HexRes.__members__ ):
            print(item + " is not a memeber")
            return False
        else:
            if item == "Wood":
                WoodCnt -= 1
            elif item == "Brick":
                BrickCnt -= 1
            elif item == "Wheat":
                WheatCnt -= 1
            elif item == "Sheep":
                SheepCnt -= 1
            elif item == "Ore":
                OreCnt -= 1
            elif item == "Desert":
                DesertCnt -= 1

    if WoodCnt != 0 or BrickCnt != 0 or WheatCnt != 0 or SheepCnt != 0 or OreCnt != 0 or DesertCnt != 0:
        print("Incorrect number of resources.")
        return False

    return True

def verifyNumArr(hexNumArr):

    for item in hexNumArr:
        try:
            value = int(item)
        except ValueError:
            print("An item other than an Int was passed")

    my_dict = {i:hexNumArr.count(i) for i in hexNumArr}

    print(my_dict)

    return True

def updateGraph(hexArray):
    hexCalcObj = HexCalculations(hexArray)

def main():
    print("---------------------------------------------------------------------------------------------------")
    print("Welcome to the CatanPicker")
    print("Please update the CatanBoard.csv with the correct board configuration before running this program")
    print("---------------------------------------------------------------------------------------------------")

    try:
        catanHexes = readCSV()
        print("Catan Board was successfully read")
    except:
        print("Catan Board had errors in it, please reinput the data and try again")
        return

    updateGraph(catanHexes)



if __name__ == "__main__":
    main()
