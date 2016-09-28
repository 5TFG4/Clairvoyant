from Node import Node
import copy

class Searching_tree:
    def __init__(self,size,empty_loc_list):
        self.empty_loc_list = empty_loc_list
        self.size = size
        self.searching_tree = None
        self.reset_searching_tree()

    def reset_searching_tree(self):
        self.searching_tree = [Node(self.size) for by_player in xrange(2)]


    def get_random_move(self,move_list_loc,player):
        cache_node = searching_tree[move_list_loc[int((-0.5*player)+0.5)]]
        cache_previous_node = self.empty_loc_list
        for list_loc in move_list_loc[1:]:
            cache_previous_node = copy.deepcopy(cache_node)
            cache_node = cache_node.get_node(list_loc)
        return cache_node.get_random_node(move_list_loc[-1],cache_previous_node)
