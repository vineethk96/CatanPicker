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

    hexResList = []
    hexNumList = []
    outerVList = []
    midVList = []
    innerVList = []
    ringNum = 0

# -- read the catan board csv --
    with open('catanBoard.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        line_count = 0

        for row in csv_reader:
            hexResList.append(row[0].title())
            hexNumList.append(row[1])

        hexResList.pop(0)
        hexNumList.pop(0)

    try:
        verifyResList(hexResList)
    except:
        print("Resources have an issue.")
        return

    try:
        verifyNumList(hexNumList)
    except:
        print("Numbers have an issue.")
        return

    return (hexResList,hexNumList)

def readNeighborCSV():

    outerVList = []
    midVList = []
    innerVList = []
    tempList = []

    with open('neighbors.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        line_count = 0

        for row in csv_reader:
            if row[0] == "outer":
                ringNum = 1
                continue
            elif row[0] == "mid":
                ringNum = 2
                continue
            elif row[0] == "inner":
                ringNum = 3
                continue

            # creates a list for the neighbors on the outside ring
            temp1 = row[0]
            if row[1] is not None:
                temp2 = row[1]
                if row[2] is not None:
                    temp3 = row[2]
                    tempList = [temp1, temp2, temp3]
                else:
                    tempList = [temp1, temp2]
            else:
                tempList = [temp1]

            #print("tempList")
            #print(tempList)
            if ringNum == 1:
                outerVList.append(tempList)
            elif ringNum == 2:
                midVList.append(tempList)
            elif ringNum == 3:
                innerVList.append(tempList)

    return (outerVList, midVList, innerVList)

def verifyResList(hexResList):
    WoodCnt = 4
    BrickCnt = 3
    WheatCnt = 4
    SheepCnt = 4
    OreCnt = 3
    DesertCnt = 1

    for item in hexResList:

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

def verifyNumList(hexNumList):

    if(len(hexNumList) != 19):
        return False

    for item in hexNumList:
        try:
            value = int(item)
        except ValueError:
            print("An item other than an Int was passed")
            return False

    if(hexNumList.count("0") != 1 or hexNumList.count("2") != 1 or hexNumList.count("12") != 1 or
        hexNumList.count("3") != 2 or hexNumList.count("4") != 2 or hexNumList.count("5") != 2 or
        hexNumList.count("6") != 2 or hexNumList.count("8") != 2 or hexNumList.count("9") != 2 or
        hexNumList.count("10") != 2 or hexNumList.count("11") != 2):
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

def createDicts(res, vals, possVals):

    iter = 0
    boardDict = {}          # initialize the dictionary

    # Each dictionary is added to the larger dictionary
    for item in res:
        tempDict = {
            "Resouce" : res[iter],
            "Value" : vals[iter],
            "Possibility" : possVals[iter]
        }

        boardDict[iter] = tempDict
        iter+=1

    #print(boardDict)
    return boardDict

def calcNeighborWeights(boardDict, outerRing, midRing, innerRing):

    bestSpot = []

    outerPossRing = neighborParser(boardDict, outerRing)
    midPossRing = neighborParser(boardDict, midRing)
    innerPossRing = neighborParser(boardDict, innerRing)

    largeOuter = max(outerPossRing)
    largeMid = max(midPossRing)
    largeInner = max(innerPossRing)

    print(largeOuter)
    print(largeMid)
    print(largeInner)

    largeOuterLoc = outerPossRing.index(largeOuter)
    largeMidLoc = midPossRing.index(largeMid)
    largeInnerLoc = innerPossRing.index(largeInner)

    print("The best spot is: ")

    if(largeOuter > largeMid) and (largeOuter > largeInner):
        print("outer ring")
        bestSpot.append(outerRing[largeOuterLoc])
    elif(largeMid > largeOuter) and (largeMid > largeInner):
        print("mid ring")
        bestSpot.append(midRing[largeMidLoc])
    elif(largeInner > largeOuter) and (largeInner > largeMid):
        print("inner ring")
        bestSpot.append(innerRing[largeInnerLoc])
    elif(largeOuter == largeInner) and (largeOuter == largeMid):
        print("Outer = Inner = Mid")
        bestSpot.append(outerRing[largeOuterLoc])
        bestSpot.append(midRing[largeMidLoc])
        bestSpot.append(innerRing[largeInnerLoc])
    elif(largeOuter == largeInner):
        print("Outer = Inner")
        bestSpot.append(outerRing[largeOuterLoc])
        bestSpot.append(innerRing[largeInnerLoc])
    elif(largeOuter == largeMid):
        print("Outer = Mid")
        bestSpot.append(outerRing[largeOuterLoc])
        bestSpot.append(midRing[largeMidLoc])
    elif(largeMid == largeInner):
        print("Mid = Inner")
        bestSpot.append(midRing[largeMidLoc])
        bestSpot.append(innerRing[largeInnerLoc])

    for spot in bestSpot:
        print("------------------------------------------------------")
        print(boardDict[int(spot[0])])
        print(boardDict[int(spot[1])])
        print(boardDict[int(spot[2])])

    return

def neighborParser(boardDict, ring):
    possRing = []
    neigh2 = False
    neigh3 = False

    for vertex in ring:

        neigh1Poss = boardDict[int(vertex[0])]["Possibility"]

        if vertex[1]:
            neigh2 = True
            neigh2Poss = boardDict[int(vertex[1])]["Possibility"]
        if vertex[2]:
            neigh3 = True
            neigh3Poss = boardDict[int(vertex[2])]["Possibility"]

        if neigh2 and neigh3:
            possRing.append(neigh1Poss + neigh2Poss + neigh3Poss)
        elif neigh2:
            possRing.append(neigh1Poss + neigh2Poss)
        else:
            possRing.append(neigh1Poss)

        neigh2 = False
        neigh3 = False

    return possRing

def main():
    print("---------------------------------------------------------------------------------------------------")
    print("Welcome to the CatanPicker")
    print("Please update the CatanBoard.csv with the correct board configuration before running this program")
    print("---------------------------------------------------------------------------------------------------")

    try:
        catanHexes = readCSV()
        print("Catan Board was successfully read.")
    except:
        print("Catan Board had errors in it, please reinput the data and try again.")
        return

    try:
        tempListCont = readNeighborCSV()
        print("Neighbors were successfully read.")
    except:
        print("Neighbors could not be read.")
        return

    outerRing = tempListCont[0]
    midRing = tempListCont[1]
    innerRing = tempListCont[2]

    dicePossList = calcDicePoss(catanHexes[1])

    #print(catanHexes[0])
    #print(catanHexes[1])
    #print(dicePossList)
    #print("Outer ----")
    #print(outerRing)
    #print("Mid ------")
    #print(midRing)
    #print("Inner ----")
    #print(innerRing)
    #print()
    #print("-------------------------------------------------------------------")
    #print()

    boardDict = createDicts(catanHexes[0], catanHexes[1], dicePossList)

    calcNeighborWeights(boardDict, outerRing, midRing, innerRing)




if __name__ == "__main__":
    main()
