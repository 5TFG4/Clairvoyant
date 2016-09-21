import random
import copy
from functools import partial
from Rule import Rule

class AI:
    def __init__(self,rule,sim_num):
        self.rule = rule
        self.sim_num = sim_num
        self.piece_score_list = None
        self.piece_win_chance_list = None
        self.reset_piece_score_list()

    def reset_piece_score_list(self):
        self.piece_score_list = [[[[0,0] for idx in xrange(self.rule.get_board().get_board_size())] for jdx in xrange(self.rule.get_board().get_board_size())]for by_player in xrange(2)]
        #print self.piece_score_list
        self.calculate_piece_win_chance_list()

    def calculate_piece_win_chance_list(self):
        #self.piece_win_chance_list = [[[0.0 for idx in xrange(self.rule.get_board().get_board_size())] for jdx in xrange(self.rule.get_board().get_board_size())]for by_player in xrange(2)]
        self.piece_win_chance_list = [[[float(loc[0])/float(loc[1]) for loc in x_row if loc[1] != 0] for x_row in by_player] for by_player in self.piece_score_list]
        [[[self.piece_win_chance_list[by_player][jdx].insert(idx,0.0)\
        for idx in xrange(len(self.piece_score_list[by_player][jdx])) if self.piece_score_list[by_player][jdx][idx][1] == 0]\
        for jdx in xrange(len(self.piece_score_list[by_player]))]\
        for by_player in xrange(len(self.piece_score_list))]
         #list1.insert(1,'x')

    def make_decision(self,board,player,player_move):
        print "*********************************************************************"
        self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
        #print board.get_empty_loc_list()
        return self.simulation(board,player,player_move)

    def update_piece_score_list(self,player,loc,win,playing):
        if win:
            self.piece_score_list[int((-0.5*player)+0.5)][loc[1]][loc[0]][0] += 1
        if playing:
            self.piece_score_list[int((-0.5*player)+0.5)][loc[1]][loc[0]][1] += 1
        self.calculate_piece_win_chance_list()

    def get_move_by_score(self):
        highest_score = max([max([max(x_row) for x_row in by_player]) for by_player in self.piece_win_chance_list])
        print highest_score
        returning_list = []
        [[[returning_list.append([idx,jdx]) for idx in xrange(len(self.piece_win_chance_list[by_player][jdx])) if self.piece_win_chance_list[by_player][jdx][idx] == highest_score]\
        for jdx in xrange(len(self.piece_win_chance_list[by_player]))]\
        for by_player in xrange(len(self.piece_win_chance_list))]
        print returning_list
        return returning_list[0]
        #try:
        #    return [loc for loc in self.rule.get_empty_loc_list()\
        #    if(self.piece_score_list[0][loc[1]][loc[0]][1] != 0 and float(self.piece_score_list[0][loc[1]][loc[0]][0])/float(self.piece_score_list[0][loc[1]][loc[0]][1]) == highest_score)\
        #    or (self.piece_score_list[1][loc[1]][loc[0]][1] != 0 and float(self.piece_score_list[1][loc[1]][loc[0]][0])/float(self.piece_score_list[1][loc[1]][loc[0]][1]) == highest_score)][0]
        #except:
        #    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        #    print self.piece_win_chance_list
        #    print highest_score

    def print_piece_score_list(self):
        print "----------------------------------------score----------------------------------------"
        for player in self.piece_score_list:
            for x_raw in player:
                print x_raw
            print '-----------------------------------------------------------------'

    def print_piece_win_chance_list(self):
        print "-------------------------------------win_chance----------------------------------------"
        for player in self.piece_win_chance_list:
            for x_raw in player:
                for x_loc in x_raw:
                    print str(x_loc) + '\t',
                print '\n'
            print '-----------------------------------------------------------------'

    def get_rule(self):
        return self.rule

    def simulate(self,loc,board,player,player_move):
        self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
        cache_move = None
        #print loc
        if loc == None:
            while self.rule.main() == 0:
                loc = self.rule.get_random_loc(self.piece_win_chance_list[int((-0.5*self.rule.get_player())+0.5)])
                self.rule.c_decision(loc)
                if cache_move == None:
                    cache_move = loc
        else:
            while self.rule.main() == 0:
                self.rule.c_decision(loc)
                if cache_move == None:
                    cache_move = loc
                loc = self.rule.get_random_loc(self.piece_win_chance_list[int((-0.5*self.rule.get_player())+0.5)])
        if self.rule.main() == player:
            self.update_piece_score_list(player,cache_move,True,True)
        else:
            self.update_piece_score_list(player,cache_move,False,True)

            #if cache_move == None:
                #print self.rule.get_board().get_board()
                #print loc
            #return cache_move

    def simulation(self,board,player,player_move):
        self.reset_piece_score_list()
        for idx in xrange(int(self.sim_num*0.1)):
            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
            partial_simulate_1 = partial(self.simulate,board = board,player = player,player_move = player_move)
            #print self.rule.get_empty_loc_list()
            map(partial_simulate_1,self.rule.get_empty_loc_list())
            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(-player),None)
            partial_simulate_2 = partial(self.simulate,board = board,player = -player,player_move = None)
            #print self.rule.get_empty_loc_list()
            map(partial_simulate_2,self.rule.get_empty_loc_list())
        for idx in xrange(int(self.sim_num*0.9)):
            self.simulate(None,board,player,player_move)
            self.simulate(None,board,-player,None)
#            move_list += map(partial_simulate,self.rule.get_empty_loc_list())+map(partial_simulate,self.rule.get_empty_loc_list())


        #print len(move_list)
#        move_list = filter(lambda move:move != None,move_list)
        #print len(move_list)

#        if len(move_list) == 0:
#            self.rule.start_new_game(copy.deepcopy(board),copy.deepcopy(player),copy.deepcopy(player_move))
#            move_list.append(self.rule.get_random_loc())
#        move_list_count = [move_list.count(move) for move in move_list]
#        returning_move = move_list[move_list_count.index(max(move_list_count))]
        returning_move = self.get_move_by_score()


        print "player " + str(player)
        print "move: " + str(returning_move)# +  with " + str(max(move_list_count)) + " times"
        self.print_piece_win_chance_list()
        self.print_piece_score_list()
        return returning_move
