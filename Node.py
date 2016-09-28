import random

class Node:
    def __init__(self,size):
        self.size = size
        self.contain = [[None for idx in xrange(self.size)] for jdx in xrange(self.size)]
        self.win_times = [0,0]
        self.play_times = [0,0]
        self.win_chance = [0.01,0.01]

    def update_win_chance(self,win,player):
        player_num = int((-0.5*player)+0.5)
        self.play_times[player_num] += 1
        if win:
            self.win_times[player_num] += 1
        if self.play_times[player_num] != 0 and float(self.win_times[player_num])/float(self.play_times[player_num]) != 0.0:
            self.win_chance[player_num] = float(self.win_times[player_num])/float(self.play_times[player_num])
        else:
            self.win_chance[player_num] = 0.01

    def get_best_move(self):
        highest_score = max([max([max([cache_node.get_win_chance()[idx] for cache_node in x_row if cache_node != None])for x_row in self.contain]) for idx in xrange(len(self.win_chance))])
        returning_list = [[jdx,idx] for kdx in xrange(len(self.win_chance)) for idx in xrange(self.size) for jdx in xrange(self.size) if self.contain[idx][jdx] != None and self.contain[idx][jdx].get_win_chance()[kdx] == highest_score]
        return [returning_list[0],highest_score]

    def get_win_times(self):
        return [[self.win_times[0],self.play_times[0]],[self.win_times[1],self.play_times[1]]]

    def get_win_chance(self):
        return self.win_chance

    def get_contain(self):
        return self.contain

    def change_contain(self,contain):
        self.contian = contain

    def add_node(self,loc):
        if self.contain[loc[1]][loc[0]] == None:
            self.contain[loc[1]][loc[0]] = Node(self.size)

    def get_empty_nodes(self):
        return [[x,y] for x in xrange(self.size) for y in xrange(self.size) if self.is_empty([x,y])]

    def get_random_node(self,player,previous_node):
        #print previous_node.get_empty_nodes()
        empty_nodes = [nodes_loc for nodes_loc in self.get_empty_nodes() if nodes_loc not in previous_node.get_empty_nodes()]
#        list(set(self.get_empty_nodes()).difference(set(previous_node.get_empty_nodes())))
        if len(empty_nodes) > 0:
            loc = random.choice(empty_nodes)
            self.contain[loc[1]][loc[0]].append(Node(self.size))
        maximum = sum([node.get_win_chance()[int((-0.5*player)+0.5)] for node_list in self.contain for node in node_list if node != None])
        if maximum > 0:
            cumulative_probability = 0.0
            key = random.uniform(0,maximum)
            for y in xrange(self.size):
                for x in xrange(self.size):
                    if self.contain[y][x] != None:
                        cumulative_probability += self.contain[y][x].get_win_chance()[int((-0.5*player)+0.5)]
                        if cumulative_probability>=key:
                            return [x,y]
#        if self.contain[loc[1]][loc[0]] == None:
#            self.contain[loc[1]][loc[0]].append(Node(self.size))
#        return loc

    def test_get_node(self,loc):
        if self.contain[loc[1]][loc[0]] == None:
            self.contain[loc[1]][loc[0]] = Node(self.size)
        return self.contain[loc[1]][loc[0]]

    def is_empty(self,loc):
        if self.contain[loc[1]][loc[0]] == None:
            return True
        else:
            return False

    def get_node(self,loc):
        if self.contain[loc[1]][loc[0]] == None:
            self.contain[loc[1]][loc[0]] = Node(self.size)
        return self.contain[loc[1]][loc[0]]
