# Here we will begin my Python script for the Catan Picker

# Let's Begin Now

import csv
import operator
#from hexCalc import HexCalculations
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
        return

    try:
        verifyNumArr(hexNumArr)
    except:
        print("Numbers have an issue.")
        return

    return (hexResArr,hexNumArr)

def verifyResArr(hexResArr):
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

    if(len(hexNumArr) != 19):
        return False

    for item in hexNumArr:
        try:
            value = int(item)
        except ValueError:
            print("An item other than an Int was passed")
            return False

    if(hexNumArr.count("0") != 1 or hexNumArr.count("2") != 1 or hexNumArr.count("12") != 1 or
        hexNumArr.count("3") != 2 or hexNumArr.count("4") != 2 or hexNumArr.count("5") != 2 or
        hexNumArr.count("6") != 2 or hexNumArr.count("8") != 2 or hexNumArr.count("9") != 2 or
        hexNumArr.count("10") != 2 or hexNumArr.count("11") != 2):
        return False

    return True

def updateGraph(hexVals):
    hexCalcObj = HexCalculations(hexVals)

    hexCalcObj.convert2Graph()

def calcDicePoss(numList):
    dicePossList = []

    for item in numList:
        if(item == "2"):
            dicePossList.append(1)
        elif(item == "3"):
            dicePossList.append(2)
        elif(item == "4"):
            dicePossList.append(3)
        elif(item == "5"):
            dicePossList.append(4)
        elif(item == "6"):
            dicePossList.append(5)
        elif(item == "8"):
            dicePossList.append(5)
        elif(item == "9"):
            dicePossList.append(4)
        elif(item == "10"):
            dicePossList.append(3)
        elif(item == "11"):
            dicePossList.append(2)
        elif(item == "12"):
            dicePossList.append(1)
        elif(item == "0"):
            dicePossList.append(0)
    return dicePossList

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

    dicePossList = calcDicePoss(catanHexes[1])

    print(catanHexes[0])
    print(catanHexes[1])
    print(dicePossList)
    #updateGraph(catanHexes)



if __name__ == "__main__":
    main()
