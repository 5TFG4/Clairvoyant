import random
import copy
from Rule import Rule

class AI:
    def __init__(self,rule,sim_num):
        self.rule = rule
        self.sim_num = sim_num

    def make_decision(self,board,player,player_move):
        return self.simulation(board,player,player_move)

    def get_rule(self):
        return self.rule

    def simulation(self,board,player,player_move):
        move_list = []
        for idx in xrange(self.sim_num/2):
            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
            cache_move = None
            while self.rule.main() == 0:
                loc = self.rule.get_random_loc()
                self.rule.c_decision(loc)
                if cache_move == None:
                    cache_move = loc
            if self.rule.main() == player:
                move_list.append(cache_move)

            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(-player),None)
            cache_move = None
            while self.rule.main() == 0:
                loc = self.rule.get_random_loc()
                self.rule.c_decision(loc)
                if cache_move == None:
                    cache_move = loc
            if self.rule.main() == -player:
                move_list.append(cache_move)

        if len(move_list) == 0:
            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
            move_list.append(self.rule.get_random_loc())
        move_list_count = [move_list.count(move) for move in move_list]
        returning_move = move_list[move_list_count.index(max(move_list_count))]
        print "********************"
        print "player " + str(player)
        print "move: " + str(returning_move) + " with " + str(max(move_list_count)) + " times"
        return returning_move
