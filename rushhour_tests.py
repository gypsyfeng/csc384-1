#import student's function
from rushhour import *

passingMark = 7

vehicle_list = [['gv', (1, 1), 2, True, True],
              ['1', (3, 1), 2, False, False],
              ['3', (4, 4), 2, False, False]]
board_size = (7, 7)
goal_entrance = (4, 1)
goal_orientation = 'E'
board_properties = (board_size, goal_entrance, goal_orientation)

s1_vehicles = [['gv', (1, 1), 2, True, True],
               ['3', (4, 4), 2, False, False],
               ['1', (3, 0), 2, False, False]]

s2_vehicles = [['gv', (1, 1), 2, True, True],
               ['1', (3, 1), 2, False, False],
               ['3', (4, 3), 2, False, False]]

s3_vehicles = [['gv', (1, 1), 2, True, True],
               ['3', (4, 4), 2, False, False],
               ['1', (3, 2), 2, False, False]]

s4_vehicles = [['gv', (1, 1), 2, True, True],
               ['1', (3, 1), 2, False, False],
               ['3', (4, 5), 2, False, False]]

s5_vehicles = [['1', (3, 1), 2, False, False],
               ['3', (4, 4), 2, False, False],
               ['gv', (0, 1), 2, True, True]]

g1_vehicles = [['gv', (3, 1), 2, True, True]]

g2_vehicles = [['gv', (4, 1), 2, True, True]]

g3_vehicles = [['gv', (4, 0), 2, False, True]]

s_heur = 2
s1_heur = 2
s2_heur = 2
s3_heur = 2
s4_heur = 2
s5_heur = 3

totalTests = 0

if __name__ == '__main__':
    s = make_init_state((7, 7), [['gv', (1, 1), 2, True, True],
              ['1', (3, 1), 2, False, False],
              ['3', (4, 4), 2, False, False]], (4, 1), 'E')

    print('''Now testing your make_init_state:
               s = make_init_state((7,7), [['gv', (0, 0), 2, True, True],
                   ['1', (2, 0), 2, False, False],
                   ['3', (3, 3), 2, False, False]], (3, 0), 'E')''')

    #compare get_vehicle_statuses() list with master list
    s_vs = s.get_vehicle_statuses()
    common_vehicles = 0
    for vehicle in vehicle_list:
        for student_vehicle in s_vs:
            if (set(student_vehicle) == set(vehicle)):
                common_vehicles += 1

    if common_vehicles == 3:
        print ("\t Vehicles correctly initialized, get_vehicle_statuses() function passed this test.")
        totalTests += 1
    else:
        print ("\t ERROR: Something went wrong with your vehicle initialization or your get_vehicle_statuses() function.")
        print('''\t For the state generated by
                    s = make_init_state((7,7), [['gv', (0, 0), 2, True, True],
                       ['1', (2, 0), 2, False, False],
                       ['3', (3, 3), 2, False, False]], (3, 0), 'E')''')
        print("\t Comparing s.get_vehicle_statuses() against the original vehicle param list should get exactly 3 vehicles in common.")
        print("\t Your method returned %d" % common_vehicles)

    #compare get_board_properties() list with master list
    s_board = s.get_board_properties()
    common_properties = 0
    for prop in board_properties:
        for student_prop in s_board:
            if (set(student_prop) == set(prop)):
                common_properties += 1

    if common_properties == 3:
        print ("\t Board correctly initialized, get_board_properties() function passed this test.")
        totalTests += 1
    else:
        print ("\t ERROR: Something went wrong with your board initialization or your get_board_properties() function.")
        print('''\t For the state generated by
                    s = make_init_state((7,7), [['gv', (0, 0), 2, True, True],
                       ['1', (2, 0), 2, False, False],
                       ['3', (3, 3), 2, False, False]], (3, 0), 'E')''')
        print("\t Comparing s.get_board_properties() against the original board param list should get exactly 3 orders in common.")
        print("\t Your method returned %d" % common_properties)

    print("--------------------------------")
    print("Now testing your successor state function:")
    print("\t Testing successors of initial state. Should output five possible states.")

    state1 = False
    state2 = False
    state3 = False
    state4 = False
    state5 = False
    totalStates = 0

    s1_vehicles_sorted = sorted(s1_vehicles)
    s2_vehicles_sorted = sorted(s2_vehicles)
    s3_vehicles_sorted = sorted(s3_vehicles)
    s4_vehicles_sorted = sorted(s4_vehicles)
    s5_vehicles_sorted = sorted(s5_vehicles)

    #test to see if all of the states are present (regardless of order)
    if(len(s.successors()) == 5):
        totalTests += 1
        for i in range(0, 5):
            #sort student sets
            student_vehicles = sorted(s.successors()[i].get_vehicle_statuses())
            student_board_properties = s.successors()[i].get_board_properties()
            if (student_vehicles == s1_vehicles_sorted and
                student_board_properties == board_properties and
                state1 == False):
                    state1 = True
                    totalStates += 1
            elif (student_vehicles == s2_vehicles_sorted and
                student_board_properties == board_properties and
                state2 == False):
                    state2 = True
                    totalStates += 1
            elif (student_vehicles == s3_vehicles_sorted and
                student_board_properties == board_properties and
                state3 == False):
                    state3 = True
                    totalStates += 1
            elif (student_vehicles == s4_vehicles_sorted and
                student_board_properties == board_properties and
                state4 == False):
                    state4 = True
                    totalStates += 1
            elif (student_vehicles == s5_vehicles_sorted and
                student_board_properties == board_properties and
                state5 == False):
                    state5 = True
                    totalStates += 1

        if(totalStates == 5):
            print ("\t 5 out of 5 states were correct for the successor function.")
            totalTests += 1
        else:
            print ("\t ERROR: Only %d out of 5 states were correct. Something's wrong with your successor function:" % totalStates)
            if (state1 == False):
                print("\t Missing state:")
                print("\t", s1_vehicles)
                print("\t", board_properties)
            if (state2 == False):
                print("\t Missing state:")
                print("\t", s2_vehicles)
                print("\t", board_properties)
            if (state3 == False):
                print("\t Missing state:")
                print("\t", s3_vehicles)
                print("\t", board_properties)
            if (state4 == False):
                print("\t Missing state:")
                print("\t", s4_vehicles)
                print("\t", board_properties)
            if (state5 == False):
                print("\t Missing state:")
                print("\t", s5_vehicles)
                print("\t", board_properties)
    else:
        print("\t ERROR: You have an incorrect number of states in your successor function.")
        print("\t We expect to have 5 states in s.successors().")
        print("\t Your function returned %d" % totalStates)

    print("--------------------------------")
    print("Now testing your heuristic:")
    if(heur_min_moves(s) == s_heur):
        totalTests += 1
        print("\t Initial state heuristic is correct.")
    else:
        print("\t Initial state heuristic wrong. Something's wrong with your heuristic.")
        print("\t heur_min_moves(s) should return %d" % s_heur)
        print("\t Your function returned %d" % heur_min_moves(s))

    heur1 = False
    heur2 = False
    heur3 = False
    heur4 = False
    heur5 = False
    totalHeurs = 0

    if (len(s.successors()) == 5):
        for i in range (0, 5):
            if (heur_min_moves(s.successors()[i]) == s1_heur and heur1 == False):
                heur1 = True
                totalHeurs += 1
            elif (heur_min_moves(s.successors()[i]) == s2_heur and heur2 == False):
                heur2 = True
                totalHeurs += 1
            elif (heur_min_moves(s.successors()[i]) == s3_heur and heur3 == False):
                heur3 = True
                totalHeurs += 1
            elif (heur_min_moves(s.successors()[i]) == s4_heur and heur4 == False):
                heur4 = True
                totalHeurs += 1
            elif (heur_min_moves(s.successors()[i]) == s5_heur and heur5 == False):
                heur5 = True
                totalHeurs += 1

        if(totalHeurs == 5):
            print ("\t 5 out of 5 tested heuristics were correct.")
            totalTests += 1
        else:
            print ("\t ERROR: Only %d out of 5 tested heuristics were correct." % totalHeurs)
            print ('''\t Calling heur_moves() on s.successors() should return heuristics for five states: 
                    %d, %d, %d, %d, and %d.''' % (s1_heur, s2_heur, s3_heur, s4_heur, s5_heur))
            if(heur1 == False):
                print("\t You are missing %d" % s1_heur)
            if(heur2 == False):
                print("\t You are missing %d" % s2_heur)
            if(heur3 == False):
                print("\t You are missing %d" % s3_heur)
            if(heur4 == False):
                print("\t You are missing %d" % s4_heur)
            if(heur5 == False):
                print("\t You are missing %d" % s5_heur)

    print("--------------------------------")
    print("Now testing your goal state test function:")
    totalGoals = 0
    missedGoal1 = False
    missedGoal2 = False
    missedGoal3 = False
    missedGoal4 = False
    missedGoal5 = False
    if rushhour_goal_fn(make_init_state((7, 7), s1_vehicles, (4, 1), 'E')) is False:
        totalGoals += 1
    else:
        missedGoal1 = True
    if rushhour_goal_fn(make_init_state((7, 7), s5_vehicles, (4, 1), 'E')) is False:
        totalGoals += 1
    else:
        missedGoal2 = True
    if rushhour_goal_fn(make_init_state((7, 7), g1_vehicles, (4, 1), 'E')) is True:
        totalGoals += 1
    else:
        missedGoal3 = True
    if rushhour_goal_fn(make_init_state((7, 7), g2_vehicles, (4, 1), 'E')) is False:
        totalGoals += 1
    else:
        missedGoal4 = True
    if rushhour_goal_fn(make_init_state((7, 7), g3_vehicles, (4, 1), 'E')) is False:
        totalGoals += 1
    else:
        missedGoal5 = True
    if totalGoals == 5:
        print ("\t Your goal state test function returned the correct value for 5 out of 5 states.")
        totalTests += 1
    else:
        print ("\t ERROR: Only %d out of 5 tested states were classified correctly by your goal function." % totalGoals)
        if missedGoal1:
            print (''' The following state was classified incorrectly:
                       ((7,7),
                       [['gv', (1, 1), 2, True, True],
                       ['3', (4, 4), 2, False, False],
                       ['1', (3, 0), 2, False, False]],
                       (4, 1), 'E')''')
        if missedGoal2:
            print (''' The following state was classified incorrectly:
                       ((7,7),
                       [['1', (3, 1), 2, False, False],
                       ['3', (4, 4), 2, False, False],
                       ['gv', (0, 1), 2, True, True]],
                       (4, 1), 'E')''')
        if missedGoal3:
            print (''' The following state was classified incorrectly:
                       ((7,7),
                       [['gv', (3, 1), 2, True, True]],
                       (4, 1), 'E')''')
        if missedGoal4:
            print (''' The following state was classified incorrectly:
                       ((7,7),
                       [['gv', (4, 1), 2, True, True]],
                       (4, 1), 'E')''')
        if missedGoal5:
            print (''' The following state was classified incorrectly:
                       ((7,7),
                       [['gv', (4, 0), 2, False, True]],
                       (4, 1), 'E')''')

    print("--------------------------------")
    if(totalTests == passingMark):
        print("All tests passed. Good job!")
    else:
        print("Some errors were found. Go back and check the output.")
