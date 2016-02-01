#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.

'''
rushhour STATESPACE
'''
#   You may add only standard python imports---i.e., ones that are automatically
#   available on CDF.
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

from search import *
from random import randint
import copy
'remember to uncomment this later!!!!!'
'from rushhour_tests import board_size, goal_entrance'

##################################################
# The search space class 'rushhour'             #
# This class is a sub-class of 'StateSpace'      #
##################################################


class rushhour(StateSpace):
    #instance
    vehicle_list = []
    max_index = 0
    prec_action = None
    
    #static variables
    board_size = ()
    goal_entrance = ()
    goal_direction = 'none'
    
    def __init__(self, action, gval, parent):
#IMPLEMENT done
        """Initialize a rushhour search state object."""
        self.action = action
        self.gval = gval
        self.parent = parent
        self.index = self.max_index
        rushhour.max_index += 1
    
    def successors(self):
#IMPLEMENT done
        '''Return list of rushhour objects that are the successors of the current object'''
        succs = []
        board = get_board(self.vehicle_list, self.get_board_properties())
        y = self.board_size[0]
        x = self.board_size[1]
        g_direction = self.goal_direction
        for j in range(0, len(self.vehicle_list)):
            'obtaining vehicle properties'
            
            ori = self.vehicle_list[j][3]
            loc = self.vehicle_list[j][1]
            l = self.vehicle_list[j][2]
            vname = self.vehicle_list[j][0]
            if ori == False:
                for i in range(1, y):
                    '''
                    print("this is the N " + str(i) + " iteration")
                    print(vname)
                    print(board[(loc[1] + i + l - 1) % y][loc[0]] )
                    for k in range(0, x):
                        for m in range(0, y):
                            print(k, m)
                            print(board[k][m])
                    print(loc[0], loc[1] + i + l - 1)
                    '''
                    if(board[(loc[1] + i + l - 1) % y][loc[0]] == '.' or board[(loc[1] + i + l - 1) % y][loc[0]] == g_direction):
                        s = rushhour("move_vehicle(" + vname + ", N)", self.gval + 1, self)
                        s.vehicle_list = copy.deepcopy(self.vehicle_list)
                        s.vehicle_list[j][1] = (loc[0],(loc[1] + i) % y)
                        succs.append(s)
                        if i >= y - 1:
                            looped = True
                        #print(s.vehicle_list)
                    else:
                        break
                for i in range(1, y):
                    '''
                    print("this is the S " + str(i) + " iteration")
                    print(vname)
                    print(board[(loc[1] - i) if (loc[1] - i) >= 0 else y + (loc[1] - i)][loc[0]])
                    print(loc[0], (loc[1] - i) if (loc[1] - i) >= 0 else y + (loc[1] - i))
                    '''
                    if((board[(loc[1] - i) if (loc[1] - i) >= 0 else y + (loc[1] - i)][loc[0]] == '.' 
                       or board[(loc[1] - i) if (loc[1] - i) >= 0 else y + (loc[1] - i)][loc[0]] 
                       == g_direction)):
                        s = rushhour("move_vehicle(" + vname + ", S)", self.gval + 1, self)
                        s.vehicle_list = copy.deepcopy(self.vehicle_list)
                        s.vehicle_list[j][1] = (loc[0], (loc[1] - i) if (loc[1] - i) >= 0 else y + (loc[1] - i))
                        succs.append(s)
                    else:
                        break
            
            else:
                for i in range(1, x):
                    '''
                    print("this is the  E " + str(i) + " iteration")
                    print(vname)
                    print(board[loc[1]][(loc[0] + i + l - 1) % x])
                    for k in range(0, x):
                        for m in range(0, y):
                            print(k, m)
                            print(board[k][m])
                            
                    print((loc[0] + i + l - 1) % x, loc[1])
                    '''
                    if(board[loc[1]][(loc[0] + i + l - 1) % x] == '.' or board[loc[1]][(loc[0] + i + l - 1) % x] == g_direction):
                        s = rushhour("move_vehicle(" + vname + ", E)", self.gval + 1, self)
                        s.vehicle_list = copy.deepcopy(self.vehicle_list)
                        s.vehicle_list[j][1] = ((loc[0] + i) % x, loc[1])
                        succs.append(s)
                        if i >= x - 1:
                            looped = True
                    else:
                        break
                for i in range(1, x):
                    '''
                    print("this is the  W " + str(i) + " iteration")
                    print(vname)
                    print(board[loc[1]][(loc[0] - i) if (loc[0] - i) >= 0 else x + (loc[0] - i)])
                    print((loc[0] - i) if (loc[0] - i) >= 0 else x + (loc[0] - i), loc[1])
                    '''
                    if((board[loc[1]][(loc[0] - i) if (loc[0] - i) >= 0 else x + (loc[0] - i)] == '.' 
                       or board[loc[1]][(loc[0] - i) if (loc[0] - i) >= 0 else x + (loc[0] - i)] 
                       == g_direction)):
                        s = rushhour("move_vehicle(" + vname + ", W)", self.gval + 1, self)
                        s.vehicle_list = copy.deepcopy(self.vehicle_list)
                        s.vehicle_list[j][1] = ((loc[0] - i) if (loc[0] - i) >= 0 else x + (loc[0] - i), loc[1])
                        succs.append(s)
                    else:
                        break
            
        return succs
                    
            
    def hashable_state(self):
#IMPLEMENT
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''

    def print_state(self):
        #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
        #and in generating sample trace output.
        #Note that if you implement the "get" routines
        #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
        #properly, this function should work irrespective of how you represent
        #your state.

        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))

        print("Vehicle Statuses")
        for vs in sorted(self.get_vehicle_statuses()):
            print("    {} is at ({}, {})".format(vs[0], vs[1][0], vs[1][1]), end="")
        board = get_board(self.get_vehicle_statuses(), self.get_board_properties())
        print('\n')
        print('\n'.join([''.join(board[i]) for i in range(len(board))]))

#Data accessor routines.

    def get_vehicle_statuses(self):
#IMPLEMENT DONE
        '''Return list containing the status of each vehicle
           This list has to be in the format: [vs_1, vs_2, ..., vs_k]
           with one status list for each vehicle in the state.
           Each vehicle status item vs_i is itself a list in the format:
                 [<name>, <loc>, <length>, <is_horizontal>, <is_goal>]
           Where <name> is the name of the robot (a string)
                 <loc> is a location (a pair (x,y)) indicating the front of the vehicle,
                       i.e., its length is counted in the positive x- or y-direction
                       from this point
                 <length> is the length of that vehicle
                 <is_horizontal> is true iff the vehicle is oriented horizontally
                 <is_goal> is true iff the vehicle is a goal vehicle
        '''
        return self.vehicle_list

    def get_board_properties(self):
#IMPLEMENT DONE
        '''Return (board_size, goal_entrance, goal_direction)
           where board_size = (m, n) is the dimensions of the board (m rows, n columns)
                 goal_entrance = (x, y) is the location of the goal
                 goal_direction is one of 'N', 'E', 'S' or 'W' indicating
                                the orientation of the goal
        '''
        return (self.board_size, self.goal_entrance, self.goal_direction)

#############################################
# heuristics                                #
#############################################


def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_min_moves(state):
#IMPLEMENT Done
    '''rushhour heuristic'''
    #We want an admissible heuristic. Getting to the goal requires
    #one move for each tile of distance.
    #Since the board wraps around, there are two different
    #directions that lead to the goal.
    #NOTE that we want an estimate of the number of ADDITIONAL
    #     moves required from our current state
    #1. Proceeding in the first direction, let MOVES1 =
    #   number of moves required to get to the goal if it were unobstructed
    #2. Proceeding in the second direction, let MOVES2 =
    #   number of moves required to get to the goal if it were unobstructed
    #
    #Our heuristic value is the minimum of MOVES1 and MOVES2 over all goal vehicles.
    #You should implement this heuristic function exactly, even if it is
    #tempting to improve it.
    
    if(rushhour_goal_fn(state) == True):
        print("here")
        return 0
    #board properties
    board = get_board(state.vehicle_list, state.get_board_properties())
    y = state.board_size[0]
    x = state.board_size[1]
    g_direction = state.goal_direction
    # vehicle properties
    ori = state.vehicle_list[0][3]
    loc = state.vehicle_list[0][1]
    l = state.vehicle_list[0][2]
    num_moves_pos = 0
    num_moves_neg = 0
    if ori == False:
        if(g_direction == "S"):            
            for i in range(1, y):
                if(board[(loc[1] + i + l - 1) % y][loc[0]] != g_direction): 
                    num_moves_pos += 1
                else:
                    num_moves_pos += 1
                    break
            for i in range(1, y):
                #checking if the south side of the vehicle is on the goal entrance
                if(board[(loc[1] - i + l - 1) % y if (loc[1] - i + l - 1) % y >= 0 
                         else y + (loc[1] - i + l - 1) % y][loc[0]] != g_direction):
                    num_moves_neg += 1
                else:
                    num_moves_neg += 1
                    break
        #north oriented goal
        else:
            for i in range(1, y):
                if(board[(loc[1] + i) % y][loc[0]] != g_direction): 
                    num_moves_pos += 1
                else:
                    num_moves_pos += 1
                    break
            for i in range(1, y):
                if(board[(loc[1] - i) % y if (loc[1] - i) % y >= 0 
                         else y + (loc[1] - i) % y][loc[0]] != g_direction):
                    num_moves_neg += 1
                else:
                    num_moves_neg += 1
                    break
    else:
        if(g_direction == "E"):            
            for i in range(1, x):
                if(board[loc[1]][(loc[0] + i + l - 1) % x] != g_direction): 
                    num_moves_pos += 1
                else:
                    num_moves_pos += 1
                    break
            for i in range(1, x):
                #checking if the east side of the vehicle is on the goal entrance
                if(board[loc[1]][(loc[0] - i + l - 1) % x if (loc[0] - i + l - 1) % x >= 0 
                         else x + (loc[0] - i + l - 1) % x] != g_direction):
                    num_moves_neg += 1
                else:
                    num_moves_neg += 1
                    break
        #west oriented goal
        else:
            for i in range(1, x):
                if(board[loc[1]][(loc[0] + i) % x] != g_direction):
                    num_moves_pos += 1
                else:
                    num_moves_pos += 1
                    break
            for i in range(1, x):
                if(board[loc[1]][(loc[0] - i) % x if (loc[0] - i) % x >= 0 
                         else x + (loc[0] - i) % x] != g_direction):
                    num_moves_neg += 1
                else:
                    num_moves_neg += 1
                    break
    print(num_moves_neg, num_moves_pos)
    return min(num_moves_neg, num_moves_pos)

def rushhour_goal_fn(state):
#IMPLEMENT DONE
    '''Have we reached a goal state'''
    #board properties
    g_direction = state.goal_direction
    y = state.board_size[0]
    x = state.board_size[1]
    #vehicle properties
    old_gv_loc = state.vehicle_list[0][1]
    ori_adjusted_gv_loc = None
    ori = state.vehicle_list[0][3]
    vlength = state.vehicle_list[0][2]
    if(ori == True):
        if(g_direction == "W"):
            return old_gv_loc == state.goal_entrance
        #if east oriented goal
        else:
            ori_adjusted_gv_loc = ((old_gv_loc[0] + vlength - 1) % x, old_gv_loc[1])
            return ori_adjusted_gv_loc == state.goal_entrance
    #if vertical
    else:
        if(g_direction == "N"):
            return old_gv_loc == state.goal_entrance
        #if south oriented goal
        else:
            ori_adjusted_gv_loc = (old_gv_loc[0], (old_gv_loc[1] + vlength - 1) % y) 
            return ori_adjusted_gv_loc == state.goal_entrance
    return False


def make_init_state(board_size, vehicle_list, goal_entrance, goal_direction):
#IMPLEMENT DONE
    '''Input the following items which specify a state and return a rushhour object
       representing this initial state.
         The state's its g-value is zero
         The state's parent is None
         The state's action is the dummy action "START"
       board_size = (m, n)
          m is the number of rows in the board
          n is the number of columns in the board
       vehicle_list = [v1, v2, ..., vk]
          a list of vehicles. Each vehicle vi is itself a list
          vi = [vehicle_name, (x, y), length, is_horizontal, is_goal] where
              vehicle_name is the name of the vehicle (string)
              (x,y) is the location of that vehicle (int, int)
              length is the length of that vehicle (int)
              is_horizontal is whether the vehicle is horizontal (Boolean)
              is_goal is whether the vehicle is a goal vehicle (Boolean)
      goal_entrance is the coordinates of the entrance tile to the goal and
      goal_direction is the orientation of the goal ('N', 'E', 'S', 'W')

   NOTE: for simplicity you may assume that
         (a) no vehicle name is repeated
         (b) all locations are integer pairs (x,y) where 0<=x<=n-1 and 0<=y<=m-1
         (c) vehicle lengths are positive integers
    '''
    s = rushhour("START", 0, None)
    s.vehicle_list = vehicle_list
    rushhour.board_size = board_size
    rushhour.goal_entrance = goal_entrance
    rushhour.goal_direction = goal_direction
    return s

########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################


def get_board(vehicle_statuses, board_properties):
    #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
    #and in generating sample trace output.
    #Note that if you implement the "get" routines
    #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
    #properly, this function should work irrespective of how you represent
    #your state.
    (m, n) = board_properties[0]
    board = [list(['.'] * n) for i in range(m)]
    for vs in vehicle_statuses:
        for i in range(vs[2]):  # vehicle length
            if vs[3]:
                # vehicle is horizontal
                board[vs[1][1]][(vs[1][0] + i) % n] = vs[0][0]
                # represent vehicle as first character of its name
            else:
                # vehicle is vertical
                board[(vs[1][1] + i) % m][vs[1][0]] = vs[0][0]
                # represent vehicle as first character of its name
    # print goal
    board[board_properties[1][1]][board_properties[1][0]] = board_properties[2]
    return board


def make_rand_init_state(nvehicles, board_size):
    '''Generate a random initial state containing
       nvehicles = number of vehicles
       board_size = (m,n) size of board
       Warning: may take a long time if the vehicles nearly
       fill the entire board. May run forever if finding
       a configuration is infeasible. Also will not work any
       vehicle name starts with a period.

       You may want to expand this function to create test cases.
    '''

    (m, n) = board_size
    vehicle_list = []
    board_properties = [board_size, None, None]
    for i in range(nvehicles):
        if i == 0:
            # make the goal vehicle and goal
            x = randint(0, n - 1)
            y = randint(0, m - 1)
            is_horizontal = True if randint(0, 1) else False
            vehicle_list.append(['gv', (x, y), 2, is_horizontal, True])
            if is_horizontal:
                board_properties[1] = ((x + n // 2 + 1) % n, y)
                board_properties[2] = 'W' if randint(0, 1) else 'E'
            else:
                board_properties[1] = (x, (y + m // 2 + 1) % m)
                board_properties[2] = 'N' if randint(0, 1) else 'S'
        else:
            board = get_board(vehicle_list, board_properties)
            conflict = True
            while conflict:
                x = randint(0, n - 1)
                y = randint(0, m - 1)
                is_horizontal = True if randint(0, 1) else False
                length = randint(2, 3)
                conflict = False
                for j in range(length):  # vehicle length
                    if is_horizontal:
                        if board[y][(x + j) % n] != '.':
                            conflict = True
                            break
                    else:
                        if board[(y + j) % m][x] != '.':
                            conflict = True
                            break
            vehicle_list.append([str(i), (x, y), length, is_horizontal, False])

    return make_init_state(board_size, vehicle_list, board_properties[1], board_properties[2])


def test(nvehicles, board_size):
    s0 = make_rand_init_state(nvehicles, board_size)
    se = SearchEngine('astar', 'full')
    #se.trace_on(2)
    final = se.search(s0, rushhour_goal_fn, heur_min_moves)

if __name__ == "__main__":
    s = make_rand_init_state(1, (4, 1))
    
    print(s.vehicle_list)
    print(s.goal_entrance)
    
    
    s.print_state()
    succs = s.successors()
    
    for s in succs:
        s.print_state()
        print(heur_min_moves(s))
    