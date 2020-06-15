from hexNode import HexNode

class HexLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        # head and tail reference the end of the linked list
        self.head = None
        self.tail = None
        return

    def createBoard(self, resourceList, numberList, dicePossList):

        hexIDList = ['h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14', 'h15', 'h16', 'h17', 'h18']
        iter = 0

        for item in hexIDList:
            node = HexNode(hexIDList[iter], resourceList[iter], numberList[iter], dicePossList[iter])



            iter+=1

        return

    def addNode(self, newNode):

        if newNode.hexID == 'h0':
            self.head = newNode
            self.tail = newNode
        elif newNode.hexID == 'h1':
            self.head.E = newNode
            newNode.W = self.head
            self.tail = newNode
        elif newNode.hexID == 'h2':
            self.tail.E = newNode
            newNode.W = self.tail
            self.tail = newNode
        elif newNode.hexID == 'h3':
            self.head.SW = newNode
            newNode.NE = self.head
            self.tail = newNode
        elif newNode.hexID == 'h4':
            self.head.SE = newNode
            newNode.NW = self.head

        # Is hard coding this really the best way to go????



        return

    def add_list_item(self, newNode):
        "add an item at the end of the list"

        # Verify if the newNode is an actual HexNode
        if not isinstance(newNode, HexNode):
            # If it isn't, create a new HexNode
            newNode = HexNode(newNode)

        # If the linked list is empty, add it into the list.
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode

        return
