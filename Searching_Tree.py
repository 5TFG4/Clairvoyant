from Node import Node
import copy

class Searching_tree:
    def __init__(self,size):
        self.searching_tree = None
        self.reset_searching_tree()

    def reset_searching_tree(self):
        self.searching_tree = [Node(size).get_node() for by_player in xrange(2)]

    def add_move(self,move_list_loc,loc):
        cache_node = copy.deepcopy(searching_tree[move_list_loc[0]])
        for list_loc in move_list_loc[1:]:
            cache_node[]
