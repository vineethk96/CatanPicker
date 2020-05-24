class HexNode:
    def __init__(self, hexID, resource, hexNum, dicePoss):
        "constructor to initiate this object"

        # store data
        self.hexID = hexID
        self.resource = resource
        self.hexNum = hexNum
        self.dicePoss = dicePoss

        # store reference (next item)
        self.NE = None
        self.E = None
        self.SE = None
        self.SW = None
        self.W = None
        self.NW = None
        return

        # CTRL + / to group comment
    # def has_value(self, value):
    #     "method to compare the value with the node data"
    #     if self.data == value:
    #         return True
    #     else:
    #         return False
