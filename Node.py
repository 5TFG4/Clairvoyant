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
        #print [player_num,self.win_times[player_num],self.play_times[player_num]],self.win_times,self.play_times
        if self.play_times[player_num] != 0 and float(self.win_times[player_num])/float(self.play_times[player_num]) != 0.0:
            self.win_chance[player_num] = float(self.win_times[player_num])/float(self.play_times[player_num])
        else:
            self.win_chance[player_num] = 0.01


        #[win_chance[idx] = self.win_times[idx]/self.play_times[idx] for idx in xrange(len(win_chance)) if player_times[idx] != 0 and self.win_times[idx]/self.play_times[idx] != 0.0]

    def get_best_move(self):
        for jdx in xrange(self.size):
            for idx in xrange(self.size):
                if self.contain[jdx][idx] != None:
                    print [idx,jdx],self.contain[jdx][idx].get_win_times(),self.contain[jdx][idx].get_win_chance()
        highest_score = max([max([max([cache_node.get_win_chance()[idx] for cache_node in x_row if cache_node != None])for x_row in self.contain]) for idx in xrange(len(self.win_chance))])
        returning_list = [[idx,jdx] for kdx in xrange(len(self.win_chance)) for idx in xrange(self.size) for jdx in xrange(self.size) if self.contain[idx][jdx] != None and self.contain[idx][jdx].get_win_chance()[kdx] == highest_score]
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

    def get_random_node(self,player):
        #print self.contain
        #if previous_node != None:
        #    new_node_pool = [[jdx,idx] for idx in xrange(len(previous_node)) for jdx in xrange(len(previous_node))\
        #    if previous_node[jdx][idx] != None and self.contain[jdx][idx] == None and [jdx,idx] != previous_loc]
        #    if len(new_node_pool) != 0:
        #        new_node_loc = random.choice(new_node_pool)
        #        self.contain[new_node_loc[0]][new_node_loc[1]].append(Node(self.size))
        #print [str(node_list) for node_list in self.contain for node in node_list]
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
        loc = [random.randint(0,self.size-1),random.randint(0,self.size-1)]
        if self.contain[loc[1]][loc[0]] == None:
            self.contain[loc[1]][loc[0]].append(Node(self.size))
        return loc

    def get_node(self,loc):
        #print loc
        if self.contain[loc[1]][loc[0]] == None:
            self.contain[loc[1]][loc[0]] = Node(self.size)
        return self.contain[loc[1]][loc[0]]
