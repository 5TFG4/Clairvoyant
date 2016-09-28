import random
import copy
import math
from functools import partial
from Rule import Rule
from Node import Node

class AI:
    def __init__(self,rule,sim_num):
        self.rule = rule
        self.sim_num = sim_num
        self.searching_tree= [Node(self.rule.get_board_size()),Node(self.rule.get_board_size())]

    def make_decision(self,board,player,player_move,last_move):
        print "********************************"
        print "player " + str(player)
        self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
        return self.simulation(board,player,player_move,last_move)

    def get_move_by_score(self):
        cache_moves = [cache_node.get_best_move() for cache_node in self.searching_tree]
        move = max(cache_moves,key = lambda cache_move:cache_move[1])
        print "move: " + str(move[0]) + ' by ' + str(move[1]) +' winning chance'
        return move[0]

    def get_rule(self):
        return self.rule

    def simulate(self,loc,board,player,player_move):
        self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
        cache_move_list= [[],[]]
        cache_node_list = [self.searching_tree[int((-0.5*self.rule.get_player())+0.5)],self.searching_tree[int((0.5*self.rule.get_player())+0.5)]]
        if loc == None:
            loc = cache_node_list[int((-0.5*self.rule.get_player())+0.5)].get_random_node(self.rule.get_player(),cache_node_list[int((0.5*self.rule.get_player())+0.5)])
        else:
            loc = loc
        while self.rule.main() == 0:
            self.rule.c_decision(loc)
            cache_move_list[int((-0.5*self.rule.get_player())+0.5)].append(loc)
            cache_node_list[int((-0.5*self.rule.get_player())+0.5)] = cache_node_list[int((-0.5*self.rule.get_player())+0.5)].get_node(loc)
            loc = cache_node_list[int((-0.5*self.rule.get_player())+0.5)].get_random_node(self.rule.get_player(),cache_node_list[int((0.5*self.rule.get_player())+0.5)])
        winner = self.rule.main()
        win = [False,False]
        if winner != -11:
            win[int((-0.5*winner)+0.5)] = True
        for idx in xrange(len(cache_move_list)):
            cache_node = self.searching_tree[idx]
            for node_loc in cache_move_list[idx]:
                cache_node.update_win_chance(win[idx],(-2*idx)+1)
                cache_node = cache_node.get_node(node_loc)

    def simulation(self,board,player,player_move,last_move):
        if len(last_move) == 2:
            self.searching_tree = [self.searching_tree[0].get_node(last_move),self.searching_tree[1].get_node(last_move)]
        [self.searching_tree[idx].get_node(loc) for loc in self.rule.get_empty_loc_list() for idx in xrange(2)]
        [self.simulate(loc,board,player,player_move) == self.simulate(loc,board,-player,None) for loc in self.rule.get_empty_loc_list() for idx in xrange(int(math.ceil(self.sim_num*0.01)))]
        [self.simulate(None,board,player,player_move) == self.simulate(None,board,-player,None) for idx in xrange(self.sim_num)]
        returning_move = self.get_move_by_score()
        self.searching_tree = [self.searching_tree[0].test_get_node(returning_move),self.searching_tree[1].test_get_node(returning_move)]
        return returning_move
