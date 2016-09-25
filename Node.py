class Node:
    def __init__(self,size):
        self.contain = [[[]for idx for idx in xrange(size)] for jdx in xrange(size)],[0,0,0.0]

    def get_contain(self):
        return self.contain

    def get_node(self,loc):
        return self.contain[loc1][loc0]
