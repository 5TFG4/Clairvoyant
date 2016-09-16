import random
import copy
from Rule import Rule

class AI:
    def __init__(self,rule,sim_num):
        self.rule = rule
        self.sim_num = sim_num
        #print "1" + str(self.rule.get_board_size())

    def make_decision(self,board,player,player_move):
        cache_board = copy.deepcopy(board)
        cache_player = copy.deepcopy(player)
        cache_player_move = copy.deepcopy(player_move)
        return self.simulation(cache_board,cache_player,cache_player_move)

    def get_rule(self):
        return self.rule

    def simulation(self,board,player,player_move):
        cache_board = copy.deepcopy(board)
        cache_player = copy.deepcopy(player)
        cache_player_move = copy.deepcopy(player_move)
        #print "empty_loc_list len 0: " + str (len(board.get_empty_loc_list()))
        move_list = []
        #print self.rule.get_board_size()
        for idx in xrange(self.sim_num):
            self.rule.start_new_game(cache_board,cache_player,cache_player_move)
            cache_move = None
            while self.rule.main() == 0:
                print board.get_board()
                print "***"
                #print len(self.rule.get_board().get_empty_loc_list())
                #print "board 2: " + str(board.get_board())
                loc = self.rule.get_board().get_random_loc()
                #print self.rule.c_decision(loc)
                self.rule.c_decision(loc)
                #    print "no"
                #    loc = [random.randint(0,self.rule.get_board_size()-1),random.randint(0,self.rule.get_board_size()-1)]
                if cache_move == None:
                    cache_move = loc
                #print "board 3: " + str(board.get_board())
            #print "board 1: " + str(board.get_board())
            if self.rule.main() == player:
                #print"2"
                move_list.append(cache_move)
        if len(move_list) == 0:
            #print "??"
            return self.simulation(board,player,player_move)


            #print "board" + str(board.get_board())
            #print self.rule.main()
        move_list_count = []
        for move in move_list:
            move_list_count.append(move_list.count(move))
        returning_move = move_list[move_list_count.index(max(move_list_count))]
        print "********************"
        print "player " + str(player)
        print "move: " + str(returning_move)
        #print 'check 1: ' + str(self.rule.get_board().is_empty(returning_move))
        #print "empty_loc_list len 1: " + str (len(self.rule.get_board().get_empty_loc_list()))
        #print 'check 2: ' + str(board.is_empty(returning_move))
        #print "empty_loc_list len 2: " + str (len(board.get_empty_loc_list()))
        return returning_move
