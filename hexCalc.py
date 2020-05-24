# HexCalculations class goes Here

from hexNode import HexNode

class HexCalculations:

    def __init__(self,hexVals):
        self.hexVals = hexVals


    def convert2Graph(self):

        hexRes = self.hexVals[0]
        hexNum = self.hexVals[1]

        # values have been recieved. Next step is to convert to a graph
        print(hexRes)
        print(hexNum)
