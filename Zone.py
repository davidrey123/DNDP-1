import Node


class Zone(Node.Node):

    # **********
    # Exercise 4(a)
    # ********** 
    def __init__(self, id):
        super().__init__(id)
        self.demand = {}
        self.thruNode = True
    
    # **********
    # Exercise 4(b)
    # ********** 
    # adds the specified demand to an internal data structure for the demand from this node to the destination
    def addDemand(self, dest, dem):
        if dest in self.demand.keys():
            self.demand[dest] = self.demand[dest] + dem
        else:
            self.demand[dest] = dem
    
    # returns the number of trips from this node to the destination
    def getDemand(self, dest):
        if dest in self.demand.keys():
            return self.demand[dest]
        else:
            return 0
    
    # **********
    # Exercise 4(c)
    # ********** 
    # returns the total number of outgoing trips from this node
    def getProductions(self):
    
        total = 0.0
        
        for s in self.demand.keys():
            total += self.demand[s]
        
        return total
    
    # **********
    # Exercise 4(d)
    # ********** 
    # returns aboolean indicating whether this node is a thru node
    def isThruNode(self):
        return self.thruNode
    
    # set a boolean indicating whether this node is a thru node
    def setThruNode(self, thru):
        self.thruNode = thru
